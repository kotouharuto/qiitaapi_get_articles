from django.urls import path
from . import views

urlpatterns = [
    # path('/home', qiita_articles_page, name='home'),  # ルートURLをホーム画面に
    path("", views.qiita_articles_page, name='home'),
]