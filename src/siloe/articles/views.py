from django.shortcuts import render

from articles.models import Article


def home_page(request):
    articles = Article.objects.all()
    return render(request, 'articles/home.html', {'articles': articles})


def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/article.html', {'article': article})
