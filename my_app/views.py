from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def first(request):
    htl="""
    <h1> First Page </h1>
    <h1> <aAsosiy Page1 </h1>
    <a href="second/"> second_page.. </a>

    """
    return HttpResponse(htl)
def second(request):
    htl="""
    <h1> Second Page <h1/>
    <h1> Ikkinchi Page <h1/>
       <a href="../"> first_page.. </a>

    """
    return HttpResponse(htl)