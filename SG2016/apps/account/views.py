from django.shortcuts import render_to_response, render, redirect
from django.views.generic import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from .models import BlogAuthor, User
from .forms import *


class AuthorDetailView(DetailView):
    # model = BlogAuthor
    # pk_url_kwarg = 'author_id'
    template_name = 'account/about_author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return BlogAuthor.objects.all()[0]


# 登录
@csrf_exempt
def do_login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                    login(request, user)
                else:
                    return render(request, 'account/failure.html', {'reason': '登录验证失败'})
                return redirect('index')
            else:
                return render(request, 'account/failure.html', {'reason': login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        print(e)
        # logger.error(e)
    return render(request, 'account/login.html', locals())  # 与render的区别？？？


# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        print(e)
        # logger.error(e)
    return redirect('index')


# 注册
@csrf_exempt
def do_register(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                # 注册
                user = User.objects.create(username=reg_form.cleaned_data["username"],
                                           email=reg_form.cleaned_data["email"],
                                           # url=reg_form.cleaned_data["url"],
                                           password=make_password(reg_form.cleaned_data["password"]), )
                user.save()

                # 登录
                user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'account/failure.html', {'reason': reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        print(e)
        # logger.error(e)
    return render(request, 'account/register.html', locals())
