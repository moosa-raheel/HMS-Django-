from django.shortcuts import render, redirect
from .models import Patient
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def patient_entry_recipe(request, id):
    try:
        patient = Patient.objects.get(pk=id)
        patient = model_to_dict(patient)
    except:
        patient = None
    return render(request,"operator/patient_entry_recipe.html", {"patient" : patient})

@login_required
def delete_patient_info(request, id):
    if request.method == "POST":
        try:
            patient = Patient.objects.get(pk=id)
            patient.delete()
            messages.success(request, "Patient Deleted Successfully")
        except:
            messages.error(request, "Something went wrong unable to delete the Patient")
    else:
        messages.error(request, "You have not Permission to do it")
    return redirect("home")    