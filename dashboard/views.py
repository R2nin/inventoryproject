from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1 style="color:blue">This is the dashboard index page</h1>')


def staff(request):
    return HttpResponse('This is the staff page')   