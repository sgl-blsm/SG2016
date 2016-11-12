from django.conf.urls import url
from .views import AuthorDetailView, do_register, do_login, do_logout

urlpatterns = [
    url(r'^about_author/$', AuthorDetailView.as_view(), name='about_author'),
    url(r'^register/$', do_register, name='register'),
    url(r'^login/$', do_login, name='login'),
    url(r'^logout/$', do_logout, name='logout'),

]
