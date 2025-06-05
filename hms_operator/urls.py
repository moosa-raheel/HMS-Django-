from django.urls import path
from .views import patient_entry_recipe

urlpatterns = [
    path("patient-recipe/<int:id>/", patient_entry_recipe, name="patient_recipe")
]
