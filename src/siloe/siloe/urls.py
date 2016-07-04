"""siloe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from articles import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', TemplateView.as_view(template_name="static_pages/about.html")),
    url(r'^service/map/$', TemplateView.as_view(template_name="static_pages/service-map.html")),
    url(r'^service/worship-vision/$', TemplateView.as_view(template_name="static_pages/service-worship-vision.html")),
    url(r'^service/dates/$', TemplateView.as_view(template_name="static_pages/service-dates.html")),
    url(r'^support/billings/$', TemplateView.as_view(template_name="static_pages/support/billings.html")),
    url(r'^support/sdm-2016/$', TemplateView.as_view(template_name="static_pages/support/sdm-2016.html")),
    url(r'^articles/tags/(\d+)/$', views.view_articles_with_tag, name='view_articles_with_tag'),
    url(r'^articles/(\d+)/$', views.view_article, name='view_article'),
    url(r'^$', views.home_page, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
