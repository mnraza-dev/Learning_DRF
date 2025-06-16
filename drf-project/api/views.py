from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from students.models import Student
from rest_framework.decorators import api_view

@api_view(['GET'])
def studentsView(request):
    if request.method == 'GET':
        # Get all data
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK )
