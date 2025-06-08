from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'region']
    fieldsets = (
        ("Personal Information", {"fields" : ["full_name", "age", "gender"]}),
        ("Professional Information", {"fields" : ["email", "phone", "region", "cnic", "prefered_doctor"]}),
        ("Important Dates", {"fields" : ["date", "time"]})
    )
    readonly_fields = ["date", "time"]
    list_filter = ("prefered_doctor", "gender")
    search_fields = ["full_name", "cnic", "phone", "email"]
    