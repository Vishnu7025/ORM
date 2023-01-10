from django.shortcuts import render
from . models import Employee,Score
from django.db.models import Avg,Sum,Max
from django.db.models import Q
# Create your views here.

def employeData(request):
    emsr = Employee.objects.all()
   
    # Score.objects.update(score=100)

    context={
        'cr':emsr,
        }
    return render(request,'home.html',context)