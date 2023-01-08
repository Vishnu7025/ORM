from django.shortcuts import render
from . models import Employee
# Create your views here.

def employeData(request):
    emsr = Employee.objects.all()
    context={'cr':emsr}
    return render(request,'home.html',context)