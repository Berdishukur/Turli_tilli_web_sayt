from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_list(request):
        htl = """
        <h1> Second Blog <h1/>
        <h1> Ikkinchi Blog <h1/>
           <a href="../"> first_page.. </a>

        """
        return HttpResponse(htl)
