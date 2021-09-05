from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def index(request):
    return render(request,'index.html')
def Fun_Data(request):
    EMPLOYEE=Employee.objects.all()
    context={
        'EMPLOYEE': EMPLOYEE
    }
    return render(request,'employee.html',context)