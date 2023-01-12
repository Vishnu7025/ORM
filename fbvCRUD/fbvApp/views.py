from django.shortcuts import render,redirect
from fbvApp.forms import StudentForm
from . models import Student
# Create your views here.
def getStudent(request):
    students = Student.objects.all()
    return render(request,'index.html',{'sr':students})

def createStudent(request):
    form = StudentForm()
    if request.method== 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'create.html',{'fr':form})
def delete(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def update(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html',{'student':student})
