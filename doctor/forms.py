from django import forms
from .models import PatientReport

class PatientSearchForm(forms.Form):
    search = forms.CharField(max_length=80 ,help_text="Enter Patient Id or his C.N.I.C number", widget=forms.TextInput(attrs={"class" : "border py-2 px-3 text-xl rounded-l-full outline-0", "type" : "search", "autocomplete" : "off"}))
    
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = PatientReport
        fields = "__all__"
        widgets = {"disease_name": forms.TextInput(attrs={"class": "border border-gray-400 w-full py-2 px-4 text-gray-700"}), "prescribed_medicines" : forms.TextInput(attrs={"class": "border border-gray-400 w-full py-2 px-4 text-gray-700"}), "additional_notes" : forms.Textarea(attrs={"class": "border border-gray-400 w-full py-2 px-4 text-gray-700 h-23"})}