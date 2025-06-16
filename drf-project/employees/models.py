from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=20, )
    emp_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    hire_date = models.DateField()
    job_title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.emp_name}  - {self.job_title}"