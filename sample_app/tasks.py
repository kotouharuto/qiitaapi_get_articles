"""
Celeryで実行する非同期タスクの定義ファイル。
Qiita記事の取得タスクを非同期処理として実装。
定期的な記事取得の自動化も行う。
"""
from celery import shared_task
from celery.schedules import crontab
import logging
from .services import fetch_qiita_articles
from .celery import app

logger = logging.getLogger(__name__)
@shared_task
def fetch_qiita_articles_task():
    """定期的な記事取得タスク"""
    success = fetch_qiita_articles()
    if not success:
        # 失敗時の通知やログ記録
        logger.error("定期的な記事取得に失敗しました")
    return success

# 毎日午前9時に実行するスケジュール設定
app.conf.beat_schedule = {
    'fetch-qiita-articles-daily': {
        'task': 'sample_app.tasks.fetch_qiita_articles_task',
        'schedule': crontab(hour=9, minute=0),
    },
}