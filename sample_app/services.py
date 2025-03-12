import requests
import os
from datetime import datetime
from app.settings import QIITA_ACCESS_TOKEN

def fetch_qiita_articles():
    from sample_app.models import QiitaArticle
    """Qiita APIから最新の記事を取得する"""
    url = "https://qiita.com/api/v2/items"
    params = {"query": "AI", "per_page": 10, "page": 1}
    headers = {"Authorization": f"Bearer {QIITA_ACCESS_TOKEN}"} if QIITA_ACCESS_TOKEN else {}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        articles = response.json()
        saved_articles = []
        for article in articles:
            obj, created = QiitaArticle.objects.update_or_create(
                url=article["url"],
                defaults={
                    "title": article["title"],
                    "created_at": datetime.strptime(article["created_at"], "%Y-%m-%dT%H:%M:%S%z"),
                    "author": article["user"]["id"]
                }
            )
            saved_articles.append(obj)
        return saved_articles
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

"""
ビジネスロジックを含むサービス層の実装ファイル。
Qiita APIを使用した記事取得の具体的な処理を定義。
"""
