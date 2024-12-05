from django.shortcuts import render, redirect
from django.http import HttpResponse

from crud.forms import EmployeeForm, EmployeeDeleteForm
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
            if Employee.objects.filter(employee_id=form.employee_id).exists():
                return render(request, 'createuser.html', {
                    "form": EmployeeForm,
                    "color": "red",
                    "created": "An Employee with this Employee ID already exists!"})
            elif len(form.first_name)>32 or len(form.last_name)>32:
                return render(request, 'createuser.html', {
                    "form": EmployeeForm,
                    "color": "red",
                    "created": "First and Last names can only be 32 characters each!"})
            else:
                return render(request, 'createuser.html', {
                    "form": EmployeeForm,
                    "color": "red",
                    "created": "There was an internal error, please try again!"})
    return render(request, 'createuser.html', {
        "form": EmployeeForm,
        "color": "green",
        "created": ""})

def deleteuser(request):
    if request.POST:
        form = EmployeeDeleteForm(request.POST)
        if form.is_valid():
            Employee.objects.filter(employee_id=int(form.cleaned_data['employee_id'].__str__())).delete()
            return render(request, 'deleteuser.html', {
                'form': EmployeeDeleteForm,
                'deleted': "Deleted!",
                'color': 'green'})
        else:
            return render(request, 'deleteuser.html', {
                'form': EmployeeDeleteForm,
                'deleted': "Error, could not delete employee with this Employee ID!",
                'color': 'red'})
    return render(request, 'deleteuser.html', {'form': EmployeeDeleteForm, 'deleted': "", 'color': 'green'})

def viewusers(request):
    Employees = Employee.objects.all()
    return render(request, 'viewusers.html', {'employees' : Employees})

def updateusers(request):
    return HttpResponse("Hello, world. You're at the polls index.")


