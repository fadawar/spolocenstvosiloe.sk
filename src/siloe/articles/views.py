from django.shortcuts import render

from articles.models import Article


def home_page(request):
    articles = Article.objects.all()
    return render(request, 'articles/home.html', {'articles': articles})


def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/article.html', {'article': article})


def view_articles_with_tag(request, tag_id):
    articles = Article.objects.filter(tags=tag_id)
    return render(request, 'articles/home.html', {'articles': articles})


def view_articles_with_tag_slug(request, slug):
    articles = Article.objects.filter(tags__slug=slug)
    return render(request, 'articles/home.html', {'articles': articles})
