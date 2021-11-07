from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import datetime
from django.conf import settings
from django.utils import timezone

GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Others'),
)


class Doctors(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    age = models.IntegerField(default=None, blank=True, null=True)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    phone = models.IntegerField(default=None, blank=True, null=True)
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES, default='F')
    specialty = models.CharField(max_length=100, default=None, blank=True, null=True)
    email = models.EmailField(max_length=100, default=None, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('doctor_detail', args=[str(self.id)])


class Nurses(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    age = models.IntegerField(default=None, blank=True, null=True)
    assigned_doctor = models.ForeignKey(Doctors, default=None, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    phone = models.CharField(max_length=100, default=None, blank=True, null=True)
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES, default='M')
    email = models.EmailField(max_length=100, default=None, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('nurse_detail', args=[str(self.id)])


class Patients(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES, default='M')
    age = models.IntegerField(blank=True, default=None, null=True)
    history = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(max_length=100, default=None, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])


class Appointments(models.Model):
    patient = models.ForeignKey(Patients, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, default=None, on_delete=models.CASCADE)
    dates = models.DateField("Date", default=None,null=True)
    time = models.TimeField('Time',default=None)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
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


class Prescriptions(models.Model):
    patient = models.ForeignKey(Patients, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, default=None, on_delete=models.CASCADE)
    date = models.DateField("Date", default=datetime.date.today)
    symptoms = models.CharField(max_length=1000)
    description = models.TextField()
    pharmacy_address = models.CharField(max_length=2000, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
