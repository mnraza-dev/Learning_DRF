from django.shortcuts import render
from django.http import HttpResponse

def studentsView(request):
    return HttpResponse("Hello, World!")