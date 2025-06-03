from django import forms
from .models import Patient

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others')
)


class PatientForm(forms.ModelForm):
    gender = forms.ChoiceField( choices=GENDER_CHOICES, widget=forms.RadioSelect, required=True)
    class Meta:
        model = Patient
        fields = ['full_name', 'age', 'gender', 'region', 'email', 'phone', 'cnic', 'prefered_doctor']
        widgets = {"full_name" : forms.TextInput(attrs={"class" : "border border-gray-400 p-2 w-full"}),"age" : forms.NumberInput(attrs={"class" : "border border-gray-400 p-2 w-full"}), "region" : forms.Select(attrs={"class" : "border border-gray-400 p-2 w-full"}), "email" : forms.EmailInput(attrs={"class" : "border border-gray-400 p-2 w-full"}),"phone" : forms.EmailInput(attrs={"class" : "border border-gray-400 p-2 w-full"}), "cnic" : forms.TextInput(attrs={"class" : "border border-gray-400 p-2 w-full"}), "prefered_doctor" : forms.Select(attrs={"class" : "border border-gray-400 p-2 w-full"})}
        labels = {"cnic" : "C.N.I.C"}