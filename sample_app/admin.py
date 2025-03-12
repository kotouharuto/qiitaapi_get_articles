"""
Django管理サイトの設定ファイル。
QiitaArticleモデルの管理画面での表示方法や検索機能を定義。
"""
from django.contrib import admin
from .models import QiitaArticle

class QiitaArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'created_at']
    search_fields = ['title']

# 重複した登録を削除し、1回だけ登録する
admin.site.register(QiitaArticle, QiitaArticleAdmin)