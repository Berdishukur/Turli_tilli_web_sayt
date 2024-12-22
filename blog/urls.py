from django.urls import path
from .views import *

urlpatterns=[
    path('',main1,name="main1"),
    path('menyu',blog_list,name="blog_list"),
    path('kitob',kitob,name="kitoblar"),
]