from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import datetime
from django.conf import settings

GENDER_CHOICES = (
    (1, 'Female'),
    (2, 'Male'),
    (3, 'Others'),
)


class Doctors(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    phone = models.CharField(max_length=100, default=None, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, default=3)
    specialty = models.CharField(max_length=100, default=None, blank=True, null=True)
    email = models.EmailField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])


class Nurses(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    assigned_doctor = models.ForeignKey(Doctors, default=None, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    phone = models.CharField(max_length=100, default=None, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, default=3)
    email = models.EmailField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('nurse_detail', args=[str(self.id)])


class Patients(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, default=3)
    age = models.IntegerField(blank=True, default=None, null=True)
    history = models.CharField(max_length=1000, blank=True, null=True)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])


class Appointments(models.Model):
    patient = models.ForeignKey(Patients, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, default=None, on_delete=models.CASCADE)
    date = models.DateField("Date", default=datetime.date.today)
    time = models.TimeField(auto_now_add=True)
    Pending = 'PD'
    Approved = 'AP'
    STATUS = (
        (Pending, 'Pending'),
        (Approved, 'Approved'),
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=Pending,
    )

    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse('index')


class Prescription(models.Model):
    patient = models.ForeignKey(Patients, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, default=None, on_delete=models.CASCADE)
    date = models.DateField("Date", default=datetime.date.today)
    Symptoms = models.CharField(max_length=100)
    Description = models.TextField()
