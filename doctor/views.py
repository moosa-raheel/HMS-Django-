from django.shortcuts import render, redirect
from base.utils import find_patient
from django.contrib import messages

# Create your views here.
def prescription(request, id_or_cnic):
    patient = find_patient(id_or_cnic)
    if not patient:
        messages.error(request, "Patient with given information not found...")
        return redirect("home")
    return render(request, "doctor/prescription.html")