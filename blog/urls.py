from django.urls import path
from .views import *

urlpatterns=[
    path('blog',blog_list,name="blog_list"),
    path('kitob',kitob,name="kitob"),
]