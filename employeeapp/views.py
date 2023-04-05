from django.shortcuts import render,redirect
from .forms import Employeeform

from .models import Employee

# Create your views here.
def update_employee(request,id):
    emp = Employee.objects.get(pk=id)
    emp.name="name"
    emp.salary=""
    emp.email="email"
    emp.save()
    return redirect('show_employee.html',action='get')


def show_employee(request):
    template_name="show_employee.html"
    el=Employee.objects.all()
    context={'employee_list':el}
    return render(request,template_name,context=context)

def del_employee(request,id):
    emp=Employee.objects.get(pk=id)
    emp.delete()
    return redirect('show_employee.html')

def add_employee(request):
    template_name="add_employee.html"
    if request.method =="POST":
        print(f"POST data:{request.POST}")
        ef=Employeeform(request.POST)
        if ef.is_valid():
            name=ef.cleaned_data['name']
            salary=ef.cleaned_data['salary']
            email=ef.cleaned_data['email']

            emp=Employee(name=name,salary=salary,email=email)
            emp.save()
        #return render(request,"success.html")
        return redirect("show_employee.html")
    else:
        ef=Employeeform()
        context={'form':ef}
        return render(request,template_name,context=context)