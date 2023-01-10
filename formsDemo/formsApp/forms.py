from django import forms

class UserRegistrationForm(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)