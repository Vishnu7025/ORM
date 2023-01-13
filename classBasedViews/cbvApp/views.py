from django.shortcuts import render
from django.views.generic  import View
from django.views.generic  import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from .models import Student
from django.urls import reverse_lazy
# Create your views here.

class StudentListView(ListView):
    model = Student
class StudentDetails(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName','lastName','testScore')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('firstName','lastName','testScore')

class StudentDeleteView(DeleteView):
    model = Student
    success_url=reverse_lazy('home')


# class GreetingView(View):
#     def get(self,request):
#         return HttpResponse("first sbv says")