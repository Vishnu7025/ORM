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



# CUser.objects.aggregate(Avg('score'))
# CUser.objects.annotate(max_score=Max('score')).filter(score=F('max_score')).first()
# CUser.objects.filter(score__lt=2).exists()
# average = CUser.objects.aggregate(Avg('score'))['score__avg']
# CUser.objects.filter(score=average)
# CUser.objects.update(score=100)
# CUser.objects.exclude(score__in=[10, 20])
# CUser.objects.all()[10:].values_list('score', flat=True)
