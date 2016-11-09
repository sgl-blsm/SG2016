from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='index'),
    url(r'^article_list/$', ArticleListView.as_view(), name='article_list'),
    url(r'^article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryArticleListView.as_view(), name='get_article_list_by_category'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagArticleListView.as_view(), name='get_article_list_by_tag'),
    url(r'^search/$', SearchArticleListView.as_view(), name='search_article_list'),
]