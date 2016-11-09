from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


# 文章分页器，对文章进行分页
def article_paginator(request, article_list):
    paginator = Paginator(article_list, 1)  # 产生一个分页器（每页两条数据）
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (InvalidPage, EmptyPage, PageNotAnInteger):
        article_list = paginator.page(1)   # 若发生异常，则返回第一页数据
    return article_list
