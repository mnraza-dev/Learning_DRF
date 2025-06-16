from django.urls import path, include
from . import views

urlpatterns = [
  path('students', views.studentsView),
  path('employees', views.Employees.as_view()),
  path('employees/<int:pk>', views.EmployeeDetail.as_view()),
  path('students/<int:pk>', views.studentDetailView),
]