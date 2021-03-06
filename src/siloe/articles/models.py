from django.db import models

from taggit.managers import TaggableManager


class Article(models.Model):
    title = models.CharField(max_length=255, default="")
    content = models.TextField(default="", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created']


class VideoArticle(Article):
    video_url = models.URLField(max_length=255, default="")
    subtitles = models.FileField(upload_to="uploads/%Y/%m/%d/", default="")


class ServiceArticle(Article):
    poster = models.FileField(upload_to="uploads/%Y/%m/%d/", default="")
    audio_url = models.URLField(max_length=255, default="", blank=True)
