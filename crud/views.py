from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.shortcuts import render
from .forms import SupportServiceForm
from .models import SupportService
from .models import SupportService
from .forms import AppointmentForm
from .models import Appointment
from .forms import FeedbackForm
from .models import Feedback
from .forms import ServiceProviderForm

def index(request):
    return render(request, 'index.html')  # 渲染主页模板



def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # 保存 student_id 到数据库
            return redirect('view_students')  # 跳转到学生列表
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})

def update_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')  # 重定向到学生列表页面
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect('view_students')
    return render(request, 'delete_student.html', {'student': student})

def create_provider(request):
    if request.method == "POST":
        form = ServiceProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_services')  # 或其他页面
    else:
        form = ServiceProviderForm()
    return render(request, 'create_provider.html', {'form': form})

# 创建支持服务
def create_support_service(request):
    if request.method == "POST":
        form = SupportServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_support_services')  # 重定向到查看支持服务页面
    else:
        form = SupportServiceForm()
    return render(request, 'create_support_service.html', {'form': form})

# 查看支持服务
def view_support_services(request):
    services = SupportService.objects.all()
    return render(request, 'view_support_services.html', {'services': services})

# 更新支持服务
def update_support_service(request, service_id):
    service = get_object_or_404(SupportService, pk=service_id)
    if request.method == "POST":
        form = SupportServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('view_support_services')  # 重定向到查看支持服务页面
    else:
        form = SupportServiceForm(instance=service)
    return render(request, 'update_support_service.html', {'form': form})

# 删除支持服务
def delete_support_service(request, service_id):
    service = get_object_or_404(SupportService, pk=service_id)
    if request.method == "POST":
        service.delete()
        return redirect('view_support_services')  # 重定向到查看支持服务页面
    return render(request, 'delete_support_service.html', {'service': service})

def create_appointment(request, service_id):
    service = get_object_or_404(SupportService, pk=service_id)
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.service = service
            appointment.save()
            return redirect('view_support_services')
    else:
        form = AppointmentForm(initial={'service': service})
    return render(request, 'create_appointment.html', {'form': form, 'service': service})

def view_appointments(request):
    appointments = Appointment.objects.all()  # 获取所有预约记录
    return render(request, 'view_appointments.html', {'appointments': appointments})


def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_feedbacks')
    else:
        form = FeedbackForm()
    return render(request, 'create_feedback.html', {'form': form})




def view_feedbacks(request):
    feedbacks = Feedback.objects.all()  # 获取所有反馈
    return render(request, 'view_feedbacks.html', {'feedbacks': feedbacks})