from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name', 'department', 'job_title', 'salary']
        labels = {'employee_id':'Employee ID',
                  'first_name':'First Name',
                  'last_name':'Last Name',
                  'department':'Department',
                  'job_title':'Job Title',
                  'salary':'Salary'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2'})


class EDCF(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.employee_id} - {obj.first_name} {obj.last_name}'

class EmployeeDeleteForm(forms.Form):
    employee_id = EDCF(queryset=Employee.objects.all(),
                       empty_label="(None)")

    class Meta:
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2'})

class EmployeeUpdateForm(forms.Form):
    employee_to_update = EDCF(queryset=Employee.objects.all(),empty_label="(None)")

    employee_id = forms.IntegerField(required=False, label='Employee ID')
    first_name = forms.CharField(required=False, label='First Name')
    last_name = forms.CharField(required=False, label='Last Name')
    department = forms.CharField(required=False, label='Department')
    job_title = forms.CharField(required=False, label='Job Title')
    salary = forms.IntegerField(required=False, label='Salary')

    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name', 'department', 'job_title', 'salary']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2'})
