from django.contrib import admin
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email', 'phone', 'city']
    search_fields = ['name', 'email', 'city']