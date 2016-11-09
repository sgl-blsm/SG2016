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


