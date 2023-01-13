from django.shortcuts import render
from django.views.generic  import View
from django.views.generic  import ListView,DetailView
from django.http import HttpResponse
from .models import Student
# Create your views here.

class StudentListView(ListView):
    model = Student
class StudentDetails(DetailView):
    model = Student








# class GreetingView(View):
#     def get(self,request):
#         return HttpResponse("first sbv says")