from django.shortcuts import render
from .models import Student
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
       json_data = request.body
       stream = io.BytesIO(json_data)
       pythondata = JSONParser().parse(stream)
       serialzer = StudentSerializer(data = pythondata)

       if serialzer.is_valid():
           serialzer.save()
           res = {'msg': 'Data Created'}
           json_data = JSONRenderer().render(res)
           return HttpResponse(json_data, content_type='application/json')

       json_data = JSONRenderer().render(serialzer.errors)
       return HttpResponse(json_data, content_type='application/json')