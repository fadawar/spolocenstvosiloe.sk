from django.db import models

from taggit.managers import TaggableManager


class Article(models.Model):
    title = models.CharField(max_length=255, default="")
    content = models.TextField(default="")
    tags = TaggableManager()


class VideoArticle(Article):
    video_url = models.URLField(max_length=255, default="")
    subtitles = models.FileField(upload_to="uploads/%Y/%m/%d/", default="")
