from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>welcome to django</h1>")

def about(request):
    return HttpResponse()
# Create your views here.
