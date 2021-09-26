from django.contrib import admin

from .models import Doctors, Patients, Prescription, Appointments,Nurses


class DoctorAdmin(admin.ModelAdmin):
    model = Doctors


admin.site.register(Doctors, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    model = Patients


admin.site.register(Patients, PatientAdmin)


class PrescriptionAdmin(admin.ModelAdmin):
    model = Prescription


admin.site.register(Prescription, PrescriptionAdmin)


class AppointmentsAdmin(admin.ModelAdmin):
    model = Appointments


admin.site.register(Appointments, AppointmentsAdmin)


class NursesAdmin(admin.ModelAdmin):
    model = Nurses


admin.site.register(Nurses, NursesAdmin)