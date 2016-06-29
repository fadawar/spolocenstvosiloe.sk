from django.core.urlresolvers import resolve
from django.test import TestCase

from articles.models import Article
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
