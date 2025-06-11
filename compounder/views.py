from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from hms_operator.models import Patient
from doctor.models import PatientReport

def prescriptions_detail(request, id_or_cnic):
    patient_obj = Patient.objects.filter(Q(pk=id_or_cnic) | Q(cnic=id_or_cnic)).first()
    patient = None
    prescriptions = None

    if patient_obj:
        patient = model_to_dict(patient_obj)
        report = PatientReport.objects.filter(patient=patient_obj).first()
        print(patient)
        if report:
            prescriptions = model_to_dict(report)

    return render(request, "compounder/prescriptions_detail.html", {
        "patient": patient,
        "prescriptions": prescriptions
    })