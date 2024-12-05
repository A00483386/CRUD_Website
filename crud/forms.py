from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
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
            self.fields[field].widget.attrs.update({'class': 'form-control'})
