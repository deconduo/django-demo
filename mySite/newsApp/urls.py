from django.conf.urls import patterns, url
from .views import ArticleList, ArticleCreate

urlpatterns = patterns('',
    url(r'^$', ArticleList.as_view(), name='articles'),
    url(r'^create/$', ArticleCreate.as_view(), name='create'),
)
