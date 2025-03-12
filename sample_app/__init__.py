"""
Celeryアプリケーションのエントリーポイント。
Celeryインスタンスをプロジェクト全体で利用可能にするための初期化ファイル。
"""
from .celery import app as celery_app

__all__ = ('celery_app',)