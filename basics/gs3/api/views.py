from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

def student_api(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data, safe=False)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)