from django.db import models

class ServiceProvider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SupportService(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.service_name


class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    service = models.ForeignKey(SupportService, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.student.name} - {self.service.service_name} on {self.appointment_date}"

class Feedback(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    service = models.ForeignKey('SupportService', on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.student} - {self.service} - {self.rating}"
