import os

import datetime
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import resolve
from django.test import TestCase

from articles.models import Article, VideoArticle, ServiceArticle
from articles.views import home_page


class HomePageTest(TestCase):
    def test_root_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_root_show_articles(self):
        article = Article.objects.create()
        article.title = 'Great title for article'
        article.content = 'This is my story'
        article.save()

        response = self.client.get('/')

        self.assertContains(response, 'Great title for article')
        self.assertContains(response, 'This is my story')
        self.assertContains(response, 'href="/articles/1/"')

    def test_root_show_tags(self):
        article = Article.objects.create()
        article.tags.add("tag1")
        article.save()

        response = self.client.get('/')

        self.assertContains(response, 'tag1')

    def test_can_show_single_article(self):
        article = Article.objects.create()
        article.title = 'Great title for article'
        article.content = 'This is my story'
        article.save()

        response = self.client.get('/articles/1/')

        self.assertContains(response, 'Great title for article')
        self.assertContains(response, 'This is my story')

    def test_order_of_articles(self):
        a1 = Article.objects.create()
        a1.save()
        a2 = Article.objects.create()
        a2.save()

        response = self.client.get('/')

        self.assertEqual(response.context['articles'][0], a2)
        self.assertEqual(response.context['articles'][1], a1)


class VideoArticleTest(TestCase):
    def test_video_articles_show_every_field(self):
        video_article = VideoArticle.objects.create()
        video_article.title = 'My nice title'
        video_article.content = 'My nice content'
        video_article.video_url = 'https://www.youtube.com/watch?v=YE7VzlLtp-4'
        directory = os.path.dirname(os.path.realpath(__file__))
        upload_file = open(directory + '/apps.py', 'rb')
        video_article.subtitles = SimpleUploadedFile(upload_file.name, upload_file.read())
        video_article.save()

        response = self.client.get('/articles/1/')

        self.assertContains(response, 'My nice title')
        self.assertContains(response, 'My nice content')
        self.assertContains(response, 'https://www.youtube.com/watch?v=YE7VzlLtp-4')


class TagsInArticleTest(TestCase):
    def test_article_has_tags(self):
        article = Article.objects.create()
        article.tags.add("tag1", "tag2", "tag3")
        article.save()

        response = self.client.get('/articles/1/')

        self.assertContains(response, 'tag1')
        self.assertContains(response, 'tag2')
        self.assertContains(response, 'tag3')

    def test_video_article_has_tags(self):
        article = VideoArticle.objects.create()
        article.tags.add("tag1")
        article.save()

        response = self.client.get('/articles/1/')

        self.assertContains(response, 'tag1')

    def test_can_filter_articles_via_tags(self):
        a1 = Article.objects.create(title="First title")
        a1.tags.add("tag1")
        a1.tags.add("tag2")
        a2 = Article.objects.create(title="Second title")
        a2.tags.add("tag1")

        r1 = self.client.get('/articles/tags/1/')
        self.assertContains(r1, a1.title)
        self.assertContains(r1, a2.title)

        r2 = self.client.get('/articles/tags/2/')
        self.assertContains(r2, a1.title)
        self.assertNotContains(r2, a2.title)

    def test_tags_are_links_to_all_articles_with_that_tag(self):
        a1 = Article.objects.create(title="First title")
        a1.tags.add('tag1', 'tag2')

        response = self.client.get('/articles/1/')

        self.assertContains(response, 'href="/articles/tags/1/"')


class ServiceArticleTest(TestCase):
    def test_service_article_show_every_field(self):
        article = ServiceArticle.objects.create(title="My title", content="My content")
        article.audio_url = 'https://www.mixcloud.com/fadawar/pavol-g%C3%A1bor%C3%ADk-o-modlitbe-chv%C3%A1l/'
        directory = os.path.dirname(os.path.realpath(__file__))
        upload_file = open(directory + '/apps.py', 'rb')
        article.poster = SimpleUploadedFile(upload_file.name, upload_file.read())
        article.save()

        response = self.client.get('/articles/1/')

        self.assertContains(response, 'My title')
        self.assertContains(response, 'My content')
        self.assertContains(response, 'https://www.mixcloud.com/fadawar/pavol-g%C3%A1bor%C3%ADk-o-modlitbe-chv%C3%A1l/')
        upload_path = datetime.date.today().strftime("uploads/%Y/%m/%d/")
        self.assertContains(response, settings.MEDIA_URL + upload_path)
