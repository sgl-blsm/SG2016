from django.db import models
from django.core.urlresolvers import reverse
from SG2016.apps.account.models import BlogAuthor


class Article(models.Model):
    STATUS_CHOICES = (
        ('p', '发布'),
        ('t', '草稿'),
        ('d', '删除'),
    )

    title = models.CharField(verbose_name='标题', max_length=200)
    summary = models.CharField(verbose_name='摘要', max_length=200, blank=True,
                               help_text="可选，若为空将摘取正文的前54个字符。")
    content = models.TextField(verbose_name='正文')
    author = models.ForeignKey(BlogAuthor, verbose_name='作者', on_delete=models.CASCADE)
    status = models.CharField(verbose_name='文章状态', max_length=1, choices=STATUS_CHOICES)
    views = models.PositiveIntegerField(verbose_name='浏览量', default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', verbose_name='标签云', blank=True)

    class Meta:
        ordering = ['-create_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.summary = self.summary or self.content[0:120]
        self.author = BlogAuthor.objects.all()[0]
        super(Article, self).save(*args, **kwargs)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    # 获取某个文章的访问url地址
    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'article_id': self.id})


# 分类模型
class Category(models.Model):
    name = models.CharField(verbose_name='分类名', max_length=10)
    order = models.IntegerField(verbose_name='排序', default=0)
    description = models.CharField(verbose_name='分类描述', max_length=120,
                                   help_text='分类描述，120字以内', blank=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # 获取某个分类下文章的数量
    def get_article_num(self):
        return Article.objects.filter(category=self, status='p').count()

    # 获取某个分类下文章列表的url地址
    def get_absolute_url(self):
        return reverse('blog:get_article_list_by_category', kwargs={'category_id': self.id})


# 标签模型
class Tag(models.Model):
    name = models.CharField(verbose_name='标签名', max_length=10)
    order = models.IntegerField(verbose_name='排序', default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # 获取某个标签下文章的数量
    def get_article_num(self):
        return Article.objects.filter(tags=self, status='p').count()

    # 获取某个标签下文章列表的url地址
    def get_absolute_url(self):
        return reverse('blog:get_article_list_by_tag', kwargs={'tag_id': self.id})


# # 网站导航模型
# class Nav(models.Model):
#     title = models.CharField(verbose_name='标题', max_length=40)
#     url = models.CharField(verbose_name='URL地址', max_length=240)
#     order = models.IntegerField(verbose_name='排序', default=0)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         ordering = ['order']
#         verbose_name = '网站导航'
#         verbose_name_plural = verbose_name


# 友情网站模型
class Link(models.Model):
    name = models.CharField(verbose_name='友情网站标题', max_length=100)
    url = models.URLField(verbose_name='友情网站链接', default='http://')
    description = models.CharField(verbose_name='友情网站描述', max_length=240,
                                   help_text='网站描述，240字以内', blank=True)
    order = models.IntegerField(verbose_name='排序', default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 广告模型
class Ad(models.Model):
    name = models.CharField('广告标题', max_length=50)
    description = models.CharField('广告描述', max_length=200)
    image = models.ImageField('广告图片', upload_to='ad/%Y/%m')
    callback_url = models.URLField('回调url', null=True, blank=True)
    order = models.IntegerField('排序', default=0)

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['order', 'name']

    def __unicode__(self):
        return self.title





