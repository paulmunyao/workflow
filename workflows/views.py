from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Using function based views to return the response
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.I'm a devops engineer")