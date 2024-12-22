from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_list(request):
        htl = """
        <h1> Second Blog <h1/>
        <h1> Ikkinchi Blog <h1/>
           <a href="kitob"> Kitoblar >>>.. </a>

        """
        return HttpResponse(htl)
def kitob(request):
        htl="""
        <h1> Kitoblar menyuse<h1/>
        < href="blog"> ..<<< oldinga</a>
        """
        return HttpResponse(htl)