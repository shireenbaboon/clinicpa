from django.contrib import admin

from .models import Doctors, Patients, Prescriptions, Appointments, Nurses
from django.http import HttpResponse
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe


class DoctorAdmin(admin.ModelAdmin):
    model = Doctors



admin.site.register(Doctors, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    model = Patients


admin.site.register(Patients, PatientAdmin)


class PrescriptionAdmin(admin.ModelAdmin):
    model = Prescriptions


admin.site.register(Prescriptions, PrescriptionAdmin)


class AppointmentsAdmin(admin.ModelAdmin):
    model = Appointments


admin.site.register(Appointments, AppointmentsAdmin)


class NursesAdmin(admin.ModelAdmin):
    model = Nurses


admin.site.register(Nurses, NursesAdmin)


def admin_doctor_pdf(obj):
    url = reverse('managements:admin_doctor_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')





