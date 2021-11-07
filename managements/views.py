import email
import io
from email import message

import canvas as canvas
from django.core import mail
from django.shortcuts import render
from django.utils import timezone
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import smtplib
from pdf_mail import sendpdf
from email.message import EmailMessage
from io import BytesIO

from .models import *
from .forms import *
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail, send_mass_mail
from django.conf import settings
from .models import Doctors

from django.http import FileResponse, HttpResponseRedirect, HttpResponse, response


def doctor_list(request):
    doctor = Doctors.objects.filter(created_date__lte=timezone.now())
    return render(request, 'doctor_list.html',
                  {'doctors': doctor})


def doctor_new(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.created_date = timezone.now()
            doctor.save()
            return redirect('managements:doctor_list')
    else:
        form = DoctorForm()
        # print("Else")
    return render(request, 'doctor_new.html', {'form': form})


def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctors, pk=pk)
    if request.method == "POST":
        # update
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.updated_date = timezone.now()
            doctor.save()
            doctor = Doctors.objects.filter(created_date__lte=timezone.now())
            return render(request, 'doctor_list.html',
                          {'doctors': doctor})
    else:
        # edit
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_edit.html', {'form': form})


def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctors, pk=pk)
    doctor.delete()
    return redirect('managements:doctor_list')


def nurse_list(request):
    nurse = Nurses.objects.filter(created_date__lte=timezone.now())
    return render(request, 'nurse_list.html',
                  {'nurses': nurse})


def nurse_new(request):
    if request.method == "POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            nurse = form.save(commit=False)
            nurse.created_date = timezone.now()
            nurse.save()
            return redirect('managements:nurse_list')
    else:
        form = NurseForm()
        # print("Else")
    return render(request, 'nurse_new.html', {'form': form})


def nurse_edit(request, pk):
    nurse = get_object_or_404(Nurses, pk=pk)
    if request.method == "POST":
        # update
        form = NurseForm(request.POST, instance=nurse)
        if form.is_valid():
            nurse = form.save(commit=False)
            nurse.updated_date = timezone.now()
            nurse.save()
            nurse = Nurses.objects.filter(created_date__lte=timezone.now())
            return render(request, 'nurse_list.html',
                          {'nurses': nurse})
    else:
        # edit
        form = NurseForm(instance=nurse)
    return render(request, 'nurse_edit.html', {'form': form})


def nurse_delete(request, pk):
    nurse = get_object_or_404(Nurses, pk=pk)
    nurse.delete()
    return redirect('managements:nurse_list')


def patient_list(request):
    patient = Patients.objects.filter(created_date__lte=timezone.now())
    return render(request, 'patient_list.html',
                  {'patients': patient})


def patient_new(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.created_date = timezone.now()
            patient.save()
            return redirect('managements:patient_list')
    else:
        form = PatientForm()
        # print("Else")
    return render(request, 'patient_new.html', {'form': form})


def patient_edit(request, pk):
    patient = get_object_or_404(Patients, pk=pk)
    if request.method == "POST":
        # update
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.updated_date = timezone.now()
            patient.save()
            patient = Patients.objects.filter(created_date__lte=timezone.now())
            return render(request, 'patient_list.html',
                          {'patients': patient})
    else:
        # edit
        form = PatientForm(instance=patient)
    return render(request, 'patient_edit.html', {'form': form})


def patient_delete(request, pk):
    patient = get_object_or_404(Patients, pk=pk)
    patient.delete()
    return redirect('managements:patient_list')


def prescription_list(request):
    prescription = Prescriptions.objects.filter(created_date__lte=timezone.now())
    return render(request, 'prescription_list.html',
                  {'prescriptions': prescription})


def prescription_new(request):
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.created_date = timezone.now()
            prescription.save()
            return redirect('managements:prescription_list')
    else:
        form = PrescriptionForm()
        # print("Else")
    return render(request, 'prescription_new.html', {'form': form})


def prescription_edit(request, pk):
    prescription = get_object_or_404(Prescriptions, pk=pk)
    if request.method == "POST":
        # update
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.updated_date = timezone.now()
            prescription.save()
            prescription = Prescriptions.objects.filter(created_date__lte=timezone.now())
            return render(request, 'prescription_list.html',
                          {'prescriptions': prescription})
    else:
        # edit
        form = PrescriptionForm(instance=prescription)
    return render(request, 'prescription_edit.html', {'form': form})


def prescription_delete(request, pk):
    prescription = get_object_or_404(Prescriptions, pk=pk)
    prescription.delete()
    return redirect('managements:prescription_list')


def appointment_list(request):
    appointment = Appointments.objects.filter(created_date__lte=timezone.now())
    return render(request, 'appointment_list.html',
                  {'appointments': appointment})


def appointment_new(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.created_date = timezone.now()
            appointment.save()
            return redirect('managements:appointment_list')
    else:
        form = AppointmentForm()
        # print("Else")
    return render(request, 'appointment_new.html', {'form': form})


def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointments, pk=pk)
    if request.method == "POST":
        # update
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.updated_date = timezone.now()
            appointment.save()
            appointment = Appointments.objects.filter(created_date__lte=timezone.now())
            return render(request, 'appointment_list.html',
                          {'appointments': appointment})
    else:
        # edit
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_edit.html', {'form': form})


def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointments, pk=pk)
    appointment.delete()
    return redirect('managements:appointment_list')


def admin_doctor_pdf(request,pk):
    doctor = get_object_or_404(Doctors, pk=pk)
    subject = f' Doctor PDF is generated'
    message = 'Please find the attached file for doctor list.'

    email = EmailMessage(subject,
                         message,
                         'shireenbaboon@gmail.com',
                         ['shireen54@gmail.com']
                         )
    html = render_to_string('doctor_pdf.html',
                            {'doctors': doctor})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'doctor_{doctor}.pdf', out.getvalue(), 'application/pdf')
    email.send()
    return render(request, 'email_sent.html',
                  {'doctors': doctor})


def admin_prescription_pdf(request,pk):
    prescription = get_object_or_404(Prescriptions, pk=pk)
    subject = f' prescription PDF is generated'
    message = 'Please find the attached file for prescription.'

    email = EmailMessage(subject,
                         message,
                         'shireenbaboon@gmail.com',
                         ['shireen54@gmail.com']
                         )
    html = render_to_string('prescription_pdf.html',
                            {'prescriptions': prescription})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'prescription_{prescription}.pdf', out.getvalue(), 'application/pdf')
    email.send()
    return render(request, 'email_sent.html',
                  {'prescriptions': prescription})


def admin_appointment_pdf(request,pk):
    appointment = get_object_or_404(Appointments, pk=pk)
    subject = f' Appointment PDF is generated'
    message = 'Please find the attached file for appointment details.'

    email = EmailMessage(subject,
                         message,
                         'shireenbaboon@gmail.com',
                         ['shireen54@gmail.com']
                         )
    html = render_to_string('appointment_pdf.html',
                            {'appointments': appointment})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'appointment_{appointment}.pdf', out.getvalue(), 'application/pdf')
    email.send()
    return render(request, 'email_sent.html',
                  {'appointments': appointment})


def admin_nurse_pdf(request,pk):
    nurse = get_object_or_404(Nurses, pk=pk)
    subject = f' Nurse PDF is generated'
    message = 'Please find the attached file for nurse details.'

    email = EmailMessage(subject,
                         message,
                         'shireenbaboon@gmail.com',
                         ['shireen54@gmail.com']
                         )
    html = render_to_string('nurse_pdf.html',
                            {'nurses': nurse})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'nurse_{nurse}.pdf', out.getvalue(), 'application/pdf')
    email.send()
    return render(request, 'email_sent.html',
                  {'nurses': nurse})


def admin_patient_pdf(request,pk):
    patient = get_object_or_404(Patients, pk=pk)
    subject = f' Patient PDF is generated'
    message = 'Please find the attached file for patient details.'

    email = EmailMessage(subject,
                         message,
                         'shireenbaboon@gmail.com',
                         ['shireen54@gmail.com']
                         )
    html = render_to_string('patient_pdf.html',
                            {'patients': patient})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'patient_{patient}.pdf', out.getvalue(), 'application/pdf')
    email.send()
    return render(request, 'email_sent.html',
                  {'patients': patient})

