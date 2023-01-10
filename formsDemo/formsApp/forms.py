from django import forms

class UserRegistrationForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField()