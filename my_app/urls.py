from django.urls import path
from .views import first,second

urlpatterns=[
    path('second/',second,name="second_page")
]