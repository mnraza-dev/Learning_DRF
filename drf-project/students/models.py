from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    branch = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    year = models.IntegerField()
    semester = models.IntegerField()
    cgpa = models.FloatField()
    is_active = models.BooleanField(default=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name