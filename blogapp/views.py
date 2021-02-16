from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    return render(request, "blogapp/blog.html")

def podcasts(request):
    return render(request, "blogapp/podcasts.html")