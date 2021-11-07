from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'managements'
urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('doctor_list', views.doctor_list, name='doctor_list'),
    path('doctor_new/', views.doctor_new, name='doctor_new'),
    path('doctor/<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctor/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),
    path('', views.nurse_list, name='nurse_list'),
    path('nurse_list', views.nurse_list, name='nurse_list'),
    path('nurse_new/', views.nurse_new, name='nurse_new'),
    path('nurse/<int:pk>/edit/', views.nurse_edit, name='nurse_edit'),
    path('nurse/<int:pk>/delete/', views.nurse_delete, name='nurse_delete'),
    path('', views.patient_list, name='patient_list'),
    path('patient_list', views.patient_list, name='patient_list'),
    path('patient_new/', views.patient_new, name='patient_new'),
    path('patient/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patient/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('', views.prescription_list, name='prescription_list'),
    path('prescription_list', views.prescription_list, name='prescription_list'),
    path('prescription_new/', views.prescription_new, name='prescription_new'),
    path('prescription/<int:pk>/edit/', views.prescription_edit, name='prescription_edit'),
    path('prescription/<int:pk>/delete/', views.prescription_delete, name='prescription_delete'),
    path('', views.appointment_list, name='appointment_list'),
    path('appointment_list', views.appointment_list, name='appointment_list'),
    path('aappointment_new/', views.appointment_new, name='appointment_new'),
    path('appointment/<int:pk>/edit/', views.appointment_edit, name='appointment_edit'),
    path('appointment/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    path('doctor_pdf/<int:pk>/pdf/',
         views.admin_doctor_pdf,
         name='doctor_pdf'),
    path('prescription_pdf/<int:pk>/pdf/',
         views.admin_prescription_pdf,
         name='prescription_pdf'),
    path('appointment_pdf/<int:pk>/pdf/',
         views.admin_appointment_pdf,
         name='appointment_pdf'),
    path('nurse_pdf/<int:pk>/pdf/',
         views.admin_nurse_pdf,
         name='nurse_pdf'),
path('patient_pdf/<int:pk>/pdf/',
         views.admin_patient_pdf,
         name='patient_pdf'),


]




