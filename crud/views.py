from django.shortcuts import render, redirect
from django.http import HttpResponse

from crud.forms import EmployeeForm
from crud.models import Employee


def index(request):
    return render(request, 'index.html')

def createuser(request):
    if request.POST:
        form = EmployeeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'createuser.html', {
                "form": EmployeeForm,
                "color": "green",
                "created": "Success!"})
        else:
            return render(request, 'createuser.html', {
                "form": EmployeeForm,
                "color": "red",
                "created": "Error!"})
    return render(request, 'createuser.html', {
        "form": EmployeeForm,
        "color": "green",
        "created": ""})

def deleteuser(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def viewusers(request):
    Employees = Employee.objects.all()
    return render(request, 'viewusers.html', {'employees' : Employees})

def updateusers(request):
    return HttpResponse("Hello, world. You're at the polls index.")


