from django.urls import path
from .views import prescriptions_detail

urlpatterns = [
    path("prescription/<id_or_cnic>/", prescriptions_detail, name="prescription_detail")
]
