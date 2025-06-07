from django.urls import path
from .views import patient_entry_recipe, delete_patient_info

urlpatterns = [
    path("patient-recipe/<int:id>/", patient_entry_recipe, name="patient_recipe"),
    path("delete-patient-info/<int:id>/", delete_patient_info, name="delete-patient-info")
]
