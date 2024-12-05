from django.forms import ModelForm
from django import forms
from .models import Employee


class EmployeeForm(ModelForm):
    employee_id = forms.NumberInput()
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    department = forms.TextInput()
    job_title = forms.TextInput()
    salary = forms.NumberInput()

    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name', 'department', 'job_title', 'salary']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})