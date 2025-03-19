"""
Celeryアプリケーションのエントリーポイント。
Celeryインスタンスをプロジェクト全体で利用可能にするための初期化ファイル。
"""
from .celery_app import app as celery_app

default_app_config = 'sample_app.apps.SampleAppConfig'

__all__ = ('celery_app',)