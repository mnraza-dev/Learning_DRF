from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import Response

@api_view
def home(request):
    return  Response({'status':200, 'msg':'Hello from django Rest framework..!'})
