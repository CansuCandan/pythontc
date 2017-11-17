# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from blog.views import gitle


urlpatterns = [
                  url(r'^gitle/$', gitle, name='gitle'),

                  url(r'^$', TemplateView.as_view(template_name='index.html', content_type='text/html')),



                  url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                  url(r'^admin/', admin.site.urls),
                  url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
                  url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
                  url(r'^manifest\.json$', TemplateView.as_view(template_name='manifest.json', content_type='application/json')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
