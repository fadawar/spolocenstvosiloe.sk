from django.shortcuts import render

from articles.models import Article


def home_page(request):
    articles = Article.objects.all()
    return render(request, 'articles/home.html-gulp', {'articles': articles})
