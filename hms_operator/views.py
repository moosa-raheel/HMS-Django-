from django.shortcuts import render
from .models import Patient
from django.forms.models import model_to_dict

def patient_entry_recipe(request, id):
    try:
        patient = Patient.objects.get(pk=id)
        patient = model_to_dict(patient)
    except:
        patient = None
    return render(request,"operator/patient_entry_recipe.html", {"patient" : patient})