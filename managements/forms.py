from django import forms
from django.forms import DateInput
from bootstrap_datepicker_plus import DatePickerInput

from .models import Doctors, Nurses, Patients, Appointments, Prescriptions
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from bootstrap_datepicker_plus import DatePickerInput, MonthPickerInput
from django.forms.widgets import DateInput, TimeInput


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ('name', 'age', 'gender', 'address', 'email', 'phone', 'specialty', 'created_date',)
        GENDER_CHOICES = (
            ('', 'Select a gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),

        )



class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurses
        fields = ('name', 'age', 'gender', 'address', 'email', 'phone', 'assigned_doctor', 'created_date',)
        GENDER_CHOICES = (
            ('', 'Select a gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),

        )



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ('name', 'age', 'gender', 'address', 'email', 'phone')
        GENDER_CHOICES = (
            ('', 'Select a gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),

        )



class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescriptions
        fields = ('patient', 'doctor', 'date', 'symptoms', 'description', 'pharmacy_address', 'created_date')
        widgets = {'date': DateInput(attrs={'type': 'date'}),
                   }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ('patient', 'doctor', 'dates', 'time', 'status')
        widgets = {'dates': forms.DateInput(attrs={'type': 'date'}),
                   'time': forms.TimeInput(attrs={'type': 'time'})}
