from django.contrib import admin
from .models import User, BlogAuthor


# 分类管理模型
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'qq', 'email')


# 个人信息管理模型
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'pen_name')

    fieldsets = (
        ('基本设置', {
            'fields': ('name', 'pen_name', 'birthday', 'gender', 'introduce', 'avatar')
        }),
        ('联系信息', {
            'fields': ('email', 'qq', 'weibo', 'github')
        }),
    )


admin.site.register(BlogAuthor, PersonalInfoAdmin)
admin.site.register(User, UserAdmin)
