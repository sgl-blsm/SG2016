from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^about_author/$', AuthorDetailView.as_view(), name='about_author'),
]
