from django.shortcuts import render
from formsApp import forms
# Create your views here.
def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    return render(request,'userRegistration.html',{'form':form})