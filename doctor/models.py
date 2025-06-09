from django.db import models
from hms_operator.models import Patient

class PatientReport(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=100)
    prescribed_medicines = models.TextField(help_text="Separate multiple medicines with commas")
    additional_notes = models.TextField(blank=True, null=True)
    report_date = models.DateField(auto_now_add=True)
    report_time = models.TimeField(auto_now_add=True)
    doctor_name = models.CharField(max_length=50) 
    def __str__(self):
        return f"{self.patient.full_name} - {self.disease_name} on {self.report_date}"