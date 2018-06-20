from django.conf.urls import url
from . import views
from weblog.feeds import BlogFeed
from weblog.apps import SETTINGS as blog_settings

app_name = 'weblog'
urlpatterns = [
    url(r'^$', views.Index, name='Index'),
    url(r'^change-language/(?P<language>[-\w]+)/$', views.ChangeLanguage, name='ChangeLanguage'),
    url(r'^(?P<year>[0-9]{4})/$', views.Index, name='ArchiveIndex'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.Index, name='ArchiveIndex'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.Index, name='CategoryIndex'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[-\w]+)/$', views.PostView, name='PostView'),
]

if blog_settings['enable_rss']:
    urlpatters += [
            url(r'^/rss/$', BlogFeed(), name='RSS'),
            url(r'^/(?P<category_slug>[-\w]+)/rss/$', BlogFeed(), name='CategoryRSS'),
            ]
