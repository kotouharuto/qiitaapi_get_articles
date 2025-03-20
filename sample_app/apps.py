from django.apps import AppConfig


class SampleAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    default_app_config = 'sample_app.apps.SampleAppConfig'

    name = 'sample_app'

"""
Djangoアプリケーションの設定ファイル。
アプリケーションの基本設定を定義。
"""
