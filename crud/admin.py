from django.contrib import admin
from .models import ServiceProvider, SupportService, Student, Appointment, Feedback

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ['provider_id', 'name', 'contact_info']

@admin.register(SupportService)
class SupportServiceAdmin(admin.ModelAdmin):
    list_display = ['service_id', 'service_name', 'description']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'name', 'age', 'email']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['appointment_id', 'student', 'service', 'appointment_date']



class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'service', 'feedback_text', 'rating')  # 根据需求列出需要显示的字段

admin.site.register(Feedback, FeedbackAdmin)