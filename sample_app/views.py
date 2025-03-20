"""
ビューの定義ファイル。
Qiita記事の取得・表示に関するエンドポイントを提供。
手動での記事取得とページ表示機能を実装。
"""

import os
import django
import sys
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator

# プロジェクトのルートディレクトリを sys.path に追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Django の設定を明示的に読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from .models import QiitaArticle
from .services import fetch_qiita_articles

def get_qiita_articles():
    """記事を取得してJSON形式で返す"""
    articles = fetch_qiita_articles()
    if articles:
        data = [{
            "title": article.title,
            "url": article.url,
            "author": article.author,
            "created_at": article.created_at
        } for article in articles]
        return {"status": "success", "articles": data}
    return {"status": "error", "message": "記事の取得に失敗しました"}

def get_articles_for_display(page=1):
    """ページネーション付きで記事を取得"""
    articles_list = QiitaArticle.objects.all().order_by('-created_at')
    paginator = Paginator(articles_list, 10)
    
    try:
        page_number = int(page)
    except ValueError:
        page_number = 1
    
    return paginator.get_page(page_number)

def qiita_articles_page(request):
    # 全記事を取得して日付順にソート
    articles_list = QiitaArticle.objects.all().order_by('-created_at')
    
    # 1ページあたり10件表示
    paginator = Paginator(articles_list, 10)
    
    # GETパラメータから現在のページ番号を取得（デフォルトは1）
    page_number = request.GET.get('page', 1)
    
    try:
        # ページ番号を整数に変換
        page_number = int(page_number)
    except ValueError:
        page_number = 1
    
    # ページオブジェクトを取得
    articles = paginator.get_page(page_number)
    
    return render(request, 'qiita_articles.html', {'articles': articles})