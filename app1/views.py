from unicodedata import name
from django.shortcuts import render


# Create your views here.

def homepage(request):
    return render(request, template_name="app1/automotive.html")
