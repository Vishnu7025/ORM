from django.shortcuts import render
from . models import Employee
# Create your views here.

def employeData(request):
    ems = Employee.objects.all()
    context={'cr':ems}
    return render(request,'home.html',context)