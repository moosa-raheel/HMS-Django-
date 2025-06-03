from django.db import models

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others')
)

REGION_CHOICES = (
    ('malir', 'Malir'),
    ('korangi', 'Korangi'),
    ('Defense', 'defense'),
    ('Bhens Colony', 'bhens colony'),
    ('Quaidabad', 'quaidabad'),
    ('sadar', 'Sadar')
)

DOCTORS = (
    ('Dr. Moosa', 'Dr. Moosa'),
    ('Dr. Fareed', 'Dr. Fareed'),
    ('Dr. Umair', 'Dr. Umair')
)

class Patient(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    prefered_doctor = models.CharField(max_length=20, choices=DOCTORS)
    cnic = models.CharField(max_length=13)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name