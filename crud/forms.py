from django import forms
from .models import Student, SupportService, ServiceProvider,Appointment
from .models import Feedback

# 学生表单
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'age', 'email']

# 支持服务表单
class SupportServiceForm(forms.ModelForm):
    class Meta:
        model = SupportService
        fields = ['service_name', 'description']

# 服务提供者表单
class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['name', 'contact_info']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['student', 'service', 'feedback_text', 'rating']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['student', 'service', 'appointment_date']  # 确保字段名称与模型一致
