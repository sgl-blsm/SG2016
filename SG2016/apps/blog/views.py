from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView, ArchiveIndexView
from .models import Article, Category, Tag
from .utils import article_paginator
from collections import OrderedDict


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = article_paginator(self.request, Article.objects.filter(status='p'))
        return article_list


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'

    def get_object(self, queryset=None):
        article = get_object_or_404(Article, id=self.kwargs['article_id'])
        article.viewed()
        return article


class CategoryArticleListView(ListView):
    template_name = 'blog/article_list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list_temp = Article.objects.filter(status='p', category_id=self.kwargs['category_id'])
        article_list = article_paginator(self.request, article_list_temp)
        return article_list


class TagArticleListView(ListView):
    template_name = 'blog/article_list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list_temp = Article.objects.filter(status='p', tags__exact=self.kwargs['tag_id'])
        article_list = article_paginator(self.request, article_list_temp)
        return article_list


class SearchArticleListView(ListView):
    template_name = 'blog/article_list.html'

    def get_queryset(self):
        search_content = self.request.GET.get('search_content')
        article_list = Article.objects.filter(status='p',title__contains=search_content)
        return article_list


def article_archive(request):
    article_list = Article.objects.filter(status='p')
    year_article_dict = OrderedDict()

    for article in article_list:
        year = article.create_time.year
        if year not in year_article_dict.keys():
            year_article_dict[year] = list()
            year_article_dict[year].append(article)
        else:
            year_article_dict[year].append(article)
    return render_to_response('blog/article_archive.html', {'year_article_dict': year_article_dict})







