"""
Celeryの設定ファイル。
Celeryアプリケーションのインスタンス作成と設定を行う。
非同期タスクの実行環境を構築。
"""
import os
from celery import Celery

# Django設定モジュールを指定
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

# ブローカーURLを環境変数から取得
BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')

# Celeryアプリケーションの設定
app = Celery('sample_app', broker=BROKER_URL)

# セキュリティ設定
app.conf.update(
    broker_use_ssl=os.environ.get('BROKER_USE_SSL', False),
    broker_pool_limit=os.environ.get('BROKER_POOL_LIMIT', 10),
    broker_connection_retry=True,
    broker_connection_retry_on_startup=True,
    broker_connection_max_retries=3,
)

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# エラーハンドリング
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30.0, check_broker_connection.s(), name='check_broker_connection')

@app.task
def check_broker_connection():
    try:
        app.connection().ensure_connection(max_retries=3)
    except Exception as e:
        # ログ出力やエラー通知を実装
        print(f"Broker connection error: {e}")