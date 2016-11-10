from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^article_list/$', ArticleListView.as_view(), name='index'),
    url(r'^article_list/$', ArticleListView.as_view(), name='article_list'),
    url(r'^article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryArticleListView.as_view(), name='get_article_list_by_category'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagArticleListView.as_view(), name='get_article_list_by_tag'),
    url(r'^search/$', SearchArticleListView.as_view(), name='search_article_list'),    # 起初的搜索方式
    url(r'^search_article/', include('haystack.urls')),
    url(r'^article_archive/$', article_archive, name='article_archive'),
]
