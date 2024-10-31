from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('This is the dashboard index page')

def staff(request):
    return HttpResponse('This is the staff page')