from django import forms
from django.contrib.auth import authenticate
from .models import User

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=70, widget=forms.TextInput(attrs={"class" : "border border-gray-400 p-2 w-full"}))
    password = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={"class" : "border border-gray-400 p-2 w-full"}))
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid Username or Password")
            return cleaned_data
            
# Signup Form 
class SignupForm(forms.ModelForm):
    c_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class" : "border border-gray-300 p-2 w-full"}))
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "role", "password", "c_password"]
        widgets = {"username" : forms.TextInput(attrs={"class" : "border border-gray-300 p-2 w-full"}), "first_name" : forms.TextInput(attrs={"class" : "border border-gray-300 p-2 w-full"}), "last_name" : forms.TextInput(attrs={"class" : "border border-gray-300 p-2 w-full"}), "email" : forms.TextInput(attrs={"class" : "border border-gray-300 p-2 w-full"}), "password" : forms.PasswordInput(attrs={"class" : "border border-gray-300 p-2 w-full"}), "role" : forms.Select(attrs={"class" : "border border-gray-300 p-2 w-full"})}
            
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        c_password = cleaned_data.get('c_password')

        if password and c_password and password != c_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data