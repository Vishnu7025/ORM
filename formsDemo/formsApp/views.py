from django.shortcuts import render
from formsApp import forms
# Create your views here.
def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    if request.method=='POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            print("FirstName",form.cleaned_data['firstName'])
            print("LastName",form.cleaned_data['lastName'])
            print("Email",form.cleaned_data['email'])

    return render(request,'userRegistration.html',{'form':form})