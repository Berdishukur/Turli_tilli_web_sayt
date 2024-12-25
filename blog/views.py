from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def main1(request):
    htl = """
        <h1> Asosiy Sahifa </h1>
        <b><a href = "menyu"> Menyular >>> ... </a></b>

        """
    return HttpResponse(htl)


def blog_list(request):
    htl = """
        <h1> Second Blog <h1/>
        <h1> Ikkinchi Blog <h1/>
           <a href="kitob"> Kitoblar >>>.. </a>
           <br/>
           <br/>
        <a href="../"> ..<<< asosiy sahifa</a>


        """
    return HttpResponse(htl)


def kitob(request):
    htl = """
        <h1> Kitoblar menyuse<h1/>
        <a href="menyu"> ..<<< oldinga</a>
        <br/>
           <br/>
        <a href="../"> ..<<< asosiy sahifa</a>
        """
    return HttpResponse(htl)