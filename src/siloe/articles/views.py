from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.conf import settings

from articles.models import Article


def home_page(request):
    articles = paginate(request, Article.objects.all())
    return render(request, 'articles/home.html', {'articles': articles})


def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/article.html', {'article': article})


def view_articles_with_tag(request, tag_id):
    articles = paginate(request, Article.objects.filter(tags=tag_id))
    return render(request, 'articles/home.html', {'articles': articles})


def view_articles_with_tag_slug(request, slug):
    articles = paginate(request, Article.objects.filter(tags__slug=slug))
    return render(request, 'articles/home.html', {'articles': articles})


def paginate(request, articles_list):
    paginator = Paginator(articles_list, settings.ARTICLES_PER_PAGE)

    page = request.GET.get('page')
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        return paginator.page(paginator.num_pages)  # If page is out of range, deliver last page of results.