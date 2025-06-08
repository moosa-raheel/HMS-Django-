import qrcode.constants
from hms_operator.forms import PatientForm
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from os import getenv
from threading import Thread
import qrcode
from pathlib import Path
import socket
from django.template.loader import render_to_string
from doctor.forms import PatientSearchForm
from hms_operator.models import Patient
from django.db.models import Q
from django.contrib import messages

class HandleUsers:
    @staticmethod
    def dispetch(request):
        if request.user.role == "operator":
            return HandleUsers.handle_operator(request)
        if request.user.role == "doctor":
            return HandleUsers.handle_doctor(request)
    
    # Operator Handler 
    @staticmethod
    def handle_operator(request):
        if request.method == "POST":
            form = PatientForm(request.POST)
            if form.is_valid():
                instance = form.save()
                qr_code_generator(instance.id)
                form = PatientForm()
                EMAIL_THREAD(patient=instance).start()
                return redirect("patient_recipe", id=instance.id)
        else:
            form = PatientForm()
        return render(request,"operator/operator.html", {"form" : form})
    
    # Doctor Handler 
    @staticmethod
    def handle_doctor(request):
        if request.method == "POST":
            form = PatientSearchForm(request.POST)
            if form.is_valid():
                search = form.cleaned_data.get("search")
                patient = find_patient(search)
                print(patient)
                if not patient:
                    messages.error(request, "User With this information Does not exist...")
                else:
                    return redirect("prescription", id_or_cnic = search)
                return redirect("home")
        else:
            form = PatientSearchForm()
        return render(request, "doctor/doctor.html", {"form" : form})
    
def send_mail(patient):
    html_message = render_to_string("email.html",context={"patient" : patient})
    subject = f"HMS Registration of {patient.full_name}"
    email = EmailMultiAlternatives(subject=subject, body=html_message, from_email=getenv("EMAIL_HOST"), to=[patient.email])
    email.content_subtype = "html"
    email.send()
   
class EMAIL_THREAD(Thread):
    def __init__(self, patient):
        self.patient = patient
        Thread.__init__(self)
    
    def run(self):
        send_mail(self.patient)
        
def qr_code_generator(id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(f"http://{get_private_ipv4()}/patient-info/{id}")
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f"{Path.cwd()}\\base\\static\\img\\qr\\{id}.png")

def get_private_ipv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80)) 
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1" 
    finally:
        s.close()
    return ip

def find_patient(id_or_cnic):
   return  Patient.objects.filter(Q(pk=id_or_cnic) | Q(cnic=id_or_cnic)).first()