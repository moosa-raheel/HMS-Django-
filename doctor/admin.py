from django.contrib import admin
from .models import PatientReport
# Register your models here.

@admin.register(PatientReport)
class PatientReportAdmin(admin.ModelAdmin):
    list_display = ["id", "patient", "disease_name"]