from django import forms

from .models import Employee
class Employeeform(forms.Form):
    name=forms.CharField(label="Employee Name",max_length=50)
    salary=forms.IntegerField(label="Employee salary",max_value=500000)
    email=forms.EmailField(label="Company Email",required=False)


class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
       # fields=['price']