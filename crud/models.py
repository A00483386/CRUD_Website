from django.db import models
from django.forms import forms


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    department = models.CharField(max_length=64)
    job_title = models.CharField(max_length=64)
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.employee_id}'