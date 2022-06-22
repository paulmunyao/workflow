from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Using function based views to return the response
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.My name is Paul Munyao.A devops Engineer")

def about(request):
    return HttpResponse("Hello, world. You're at the polls about. You're at Google Analytics")