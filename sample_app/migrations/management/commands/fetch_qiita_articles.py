"""
カスタム管理コマンドの定義ファイル。
'python manage.py fetch_qiita_articles'で実行可能なQiita記事取得コマンドを実装。
"""
# services.py
from django.core.cache import cache
from typing import Optional, List
from sample_app import services
from sample_app import models
import logging
logger = logging.getLogger(__name__)

class QiitaService:
    @staticmethod
    def fetch_and_save_articles() -> bool:
        """記事を取得してDBに保存する"""
        try:
            articles = services.fetch_qiita_articles()
            if articles:
                return True
            return False
        except Exception as e:
            logger.error(f"記事の取得に失敗: {e}")
            return False

    @staticmethod
    def get_cached_articles() -> List[models.QiitaArticle]:
        """キャッシュされた記事を取得"""
        cache_key = 'qiita_articles'
        articles = cache.get(cache_key)
        if not articles:
            articles = models.QiitaArticle.objects.all()
            cache.set(cache_key, articles, timeout=3600)  # 1時間キャッシュ
        return articles