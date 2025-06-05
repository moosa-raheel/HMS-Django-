import qrcode.constants
from hms_operator.forms import PatientForm
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from os import getenv
from threading import Thread
import qrcode
from pathlib import Path
import socket

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
                email = form.cleaned_data.get("email")
                instance = form.save()
                qr_code_generator(instance.id)
                form = PatientForm()
                EMAIL_THREAD(email=email).start()
                return redirect("patient_recipe", id=instance.id)
        else:
            form = PatientForm()
        return render(request,"operator/operator.html", {"form" : form})
    
def send_mail(to_email):
   email = EmailMessage(subject="Checking", body="It's Me Moosa", from_email=getenv("EMAIL_HOST"), to=[to_email])
   email.content_subtype = "html"
   email.send()
   
class EMAIL_THREAD(Thread):
    def __init__(self, email):
        self.to_email = email
        Thread.__init__(self)
    
    def run(self):
        send_mail(self.to_email)
        
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