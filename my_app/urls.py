from django.urls import path
from .views import first,second

urlpatterns=[
    path('',first,name="first_page"),
]