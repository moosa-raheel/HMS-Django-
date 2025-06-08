from django.urls import path
from .views import prescription

urlpatterns = [
    path("prescription/<id_or_cnic>/", prescription, name="prescription")
]
