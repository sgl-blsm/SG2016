from django.shortcuts import render_to_response
from django.views.generic import DetailView
from .models import BlogAuthor
from .forms import *


class AuthorDetailView(DetailView):
    # model = BlogAuthor
    # pk_url_kwarg = 'author_id'
    template_name = 'account/about_author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return BlogAuthor.objects.all()[0]


def do_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            qq = login_form.cleaned_data['qq']
            password = login_form.cleaned_data['password']
        #     未完，待续（自定义验证后端）
        else:
            return render_to_response('account/login.html', {'error_message': login_form.errors})
    else:
        login_form = LoginForm()
        return render_to_response('account/login.html', locals())


# # 注销
# def do_logout(request):
#     try:
#         logout(request)
#     except Exception as e:
#         print e
#         logger.error(e)
#     return redirect(request.META['HTTP_REFERER'])
#
# # 注册
# def do_reg(request):
#     try:
#         if request.method == 'POST':
#             reg_form = RegForm(request.POST)
#             if reg_form.is_valid():
#                 # 注册
#                 user = User.objects.create(username=reg_form.cleaned_data["username"],
#                                     email=reg_form.cleaned_data["email"],
#                                     url=reg_form.cleaned_data["url"],
#                                     password=make_password(reg_form.cleaned_data["password"]),)
#                 user.save()
#
#                 # 登录
#                 user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
#                 login(request, user)
#                 return redirect(request.POST.get('source_url'))
#             else:
#                 return render(request, 'failure.html', {'reason': reg_form.errors})
#         else:
#             reg_form = RegForm()
#     except Exception as e:
#         logger.error(e)
#     return render(request, 'reg.html', locals())
#
# # 登录
# def do_login(request):
#     try:
#         if request.method == 'POST':
#             login_form = LoginForm(request.POST)
#             if login_form.is_valid():
#                 # 登录
#                 username = login_form.cleaned_data["username"]
#                 password = login_form.cleaned_data["password"]
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
#                     login(request, user)
#                 else:
#                     return render(request, 'failure.html', {'reason': '登录验证失败'})
#                 return redirect(request.POST.get('source_url'))
#             else:
#                 return render(request, 'failure.html', {'reason': login_form.errors})
#         else:
#             login_form = LoginForm()
#     except Exception as e:
#         logger.error(e)
#     return render(request, 'login.html', locals())



