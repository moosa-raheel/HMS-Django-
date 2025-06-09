from django.shortcuts import render, redirect
from base.utils import find_patient
from django.contrib import messages
from .forms import PrescriptionForm
from .models import PatientReport

from django.contrib import messages

def prescription(request, id_or_cnic):
    patient = find_patient(id_or_cnic)
    if not patient:
        messages.error(request, "Patient with given information not found...")
        return redirect("home")
    try:
        prescription_instance = PatientReport.objects.get(patient=patient)
    except PatientReport.DoesNotExist:
        prescription_instance = None
    if request.method == "POST":
        data = request.POST.dict()
        data['doctor_name'] = f"Dr. {request.user.first_name}"
        data['patient'] = patient.id 
        if prescription_instance:
            form = PrescriptionForm(data, instance=prescription_instance)
        else:
            form = PrescriptionForm(data)
        if form.is_valid():
            form.save()
            messages.success(request, "Prescription submitted successfully.")
            return redirect("home")
    else:
        form = PrescriptionForm(instance=prescription_instance)

    return render(request, "doctor/prescription.html", {"patient": patient, "form": form})
