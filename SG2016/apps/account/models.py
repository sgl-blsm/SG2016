from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
import datetime


# 用户模型：采用继承的方式来扩展用户信息
class User(AbstractUser):
    avatar = models.ImageField(verbose_name='头像', upload_to='avatars', default='avatars/default.png',
                               null=True, blank=False)
    qq = models.CharField(verbose_name='QQ号码', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 作者信息模型
class BlogAuthor(models.Model):
    GENDER_CHOICES = (
        ('M', '男'), ('F', '女'),
    )

    name = models.CharField(verbose_name='姓名', max_length=10, null=False, blank=False)
    pen_name = models.CharField(verbose_name='笔名', max_length=20, null=False, blank=False)
    birthday = models.DateField(verbose_name='生日', auto_now_add=False, default=datetime.datetime.now)
    gender = models.CharField(verbose_name='性别', max_length=2, default='M', choices=GENDER_CHOICES)
    introduce = models.TextField(verbose_name='个人简介', default=' ... ', null=True)
    avatar = models.ImageField(verbose_name='肖像', upload_to='avatars', null=True, blank=False)
    email = models.EmailField(verbose_name='邮箱', max_length=64, default='888888@qq.com')
    qq = models.CharField(verbose_name='QQ', max_length=64,)
    weibo = models.CharField(verbose_name='微博', max_length=255, default='http://weibo.com', null=True)
    github = models.CharField(verbose_name='GitHub', max_length=255, default='https://github.com', null=True)

    class Meta:
        verbose_name = '博客作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('account:about_author', kwargs={'author_id': self.id})
        return reverse('account:about_author')










