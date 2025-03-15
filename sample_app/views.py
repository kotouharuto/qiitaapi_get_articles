"""
ビューの定義ファイル。
Qiita記事の取得・表示に関するエンドポイントを提供。
手動での記事取得とページ表示機能を実装。
"""

from sample_app.services import fetch_qiita_articles
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import QiitaArticle
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_qiita_articles(request):
    """API endpoint for fetching articles"""
    articles = fetch_qiita_articles()
    data = [{
        "title": article.title,
        "url": article.url,
        "author": article.author,
        "created_at": article.created_at
    } for article in articles]
    return JsonResponse({"status": "success", "articles": data})

# def qiita_articles_page(request):
#     """記事一覧ページの表示"""
#     articles = fetch_qiita_articles()
#     return render(request, 'qiita_articles.html', {'articles': articles})

# def home(request):
#     articles_list = fetch_qiita_articles().order_by('-created_at')
#     # articles_list = QiitaArticle.objects.all().order_by('-created_at')  # 記事を日付順にソート
#     paginator = Paginator(articles_list, 20)  # 1ページに20件表示

#     page_number = request.GET.get('page')
#     articles = paginator.get_page(page_number)

#     return render(request, 'qiita_articles.html', {'articles': articles})

def qiita_articles_page(request):
    # 全記事を取得して日付順にソート
    articles_list = QiitaArticle.objects.all().order_by('-created_at')
    
    # 1ページあたり10件表示
    paginator = Paginator(articles_list, 20)
    
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