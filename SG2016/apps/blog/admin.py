from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import *


# 自定义ArticleAdminForm
class ArticleAdminFrom(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = '__all__'


# 文章模型定制
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminFrom
    list_display = ('title', 'author', 'status', 'views')


# 分类模型定制
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'description')

    fieldsets = (
        ('基本设置', {
            'fields': ('name', 'description', 'order')
        }),
    )


# 标签模型定制
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')

    fieldsets = (
        ('基本设置', {
            'fields': ('name', 'order')
        }),
    )


# 友情链接模型定制
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'url')

    fieldsets = (
        ('基本设置', {
            'fields': ('name', 'description', 'url', 'order')
        }),
    )


# 广告模型定制
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')

    fieldsets = (
        ('基本设置', {
            'fields': ('name', 'order', 'description', 'image', 'callback_url')
        }),
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Ad, AdAdmin)
