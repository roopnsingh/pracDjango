# from django.shortcuts import render
from django.http import HttpResponse

def landing(_request):
    return HttpResponse("Hello, world. This is the landing page from mysite")