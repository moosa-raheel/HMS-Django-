from django import forms

class PatientSearchForm(forms.Form):
    search = forms.CharField(max_length=80 ,help_text="Enter Patient Id or his C.N.I.C number", widget=forms.TextInput(attrs={"class" : "border py-2 px-3 text-xl rounded-l-full outline-0", "type" : "search", "autocomplete" : "off"}))