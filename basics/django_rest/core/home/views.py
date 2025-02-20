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

    if request.data['age'] < 18:
        return Response({
            'status': 403,
            'payload': [],
            'message': 'age should be greater than 18'
        })
    
    if not serializer.is_valid():
        Response({
            'status': 403,
            'payload': [],
            'message': 'something went wrong'	
        })
    serializer.save()
    print(data)
    return Response({'status':200, 'payload': serializer.data, 'message': 'success'})