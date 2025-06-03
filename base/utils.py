from hms_operator.forms import PatientForm
from django.shortcuts import render

class HandleUsers:
    @staticmethod
    def dispetch(request):
        if request.user.role == "operator":
            return HandleUsers.handle_operator(request)
    
    @staticmethod
    def handle_operator(request):
        if request.method == "POST":
            form = PatientForm(request.POST)
            if form.is_valid():
                form.save()
                form = PatientForm()
        else:
            form = PatientForm()
        return render(request,"operator/operator.html", {"form" : form})