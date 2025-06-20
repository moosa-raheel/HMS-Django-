from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("", include("base.urls")),
    path("operator/", include("hms_operator.urls")),
    path("doctor/", include("doctor.urls")),
    path("compounder/", include("compounder.urls")),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
