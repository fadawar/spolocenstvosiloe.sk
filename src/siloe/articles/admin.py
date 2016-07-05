from django.contrib import admin

from articles.models import Article, VideoArticle, ServiceArticle

admin.site.register(Article)
admin.site.register(VideoArticle)
admin.site.register(ServiceArticle)
