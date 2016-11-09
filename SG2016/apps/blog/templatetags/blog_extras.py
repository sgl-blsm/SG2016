from django import template
from ..models import Category, Tag

register = template.Library()


@register.inclusion_tag('blog/category_list.html', takes_context=True)
def get_categories(context):
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('blog/tag_cloud.html', takes_context=True)
def get_tags(context):
    tags = Tag.objects.all().all()
    return {'tags': tags}
