from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])	
def home(request):
    student_data = Student.objects.all()
    serializer = StudentSerializer(student_data, many=True)
    return  Response({'status':200, 'payload': serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        Response({
            'status': 403,
            'payload': [],
            'message': 'something went wrong'	
        })
    serializer.save()

    print(data)
    return Response({'status':200, 'payload': serializer.data, 'message': 'success'})

@api_view(['PATCH'])
def update_student(request, id ):
    try:
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj, data=request.data, partial=True)
        if not serializer.is_valid():
            Response({
                'status': 403,
                'payload': [],
                'message': 'something went wrong'	
            })
        serializer.save()
        return Response({'status':200, 'payload': serializer.data, 'message': 'success'})
    except Exception as e:
        return Response({'status':403, 'payload': [], 'message': 'something went wrong'})
    