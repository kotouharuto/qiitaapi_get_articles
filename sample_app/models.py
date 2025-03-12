from django.db import models

"""
データベースモデルの定義ファイル。
QiitaArticleモデルの構造とフィールドを定義。
"""

class QiitaArticle(models.Model):
 title = models.CharField(max_length=255)
 url = models.URLField(unique=True)
 created_at = models.DateTimeField()
 author = models.CharField(max_length=100)
 
 def __str__(self):
     return self.title