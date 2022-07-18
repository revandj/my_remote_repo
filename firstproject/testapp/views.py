from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    print(type(request))
    s = '<h1>Dont feel Difficult... Django is very easy.. Good Framework</h1>'
    return HttpResponse(s)
