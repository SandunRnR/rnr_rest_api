from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.ShowAllMessages, name='show-all-messages'),
    path('messages/patient/', views.PatientPostMessage, name='patient-post-message'),
    path('messages/doctor/', views.DoctorPostMessage, name='doctor-post-message'),
    path('messages/patient/get/<int:message_id>/', views.PatientGetMessage, name='patient-get-message'),
    # path('messages/patient/get/', views.PatientGetMessage, name='patient-get-message'),
    path('messages/doctor/get/', views.DoctorGetMessage, name='doctor-get-message'),
]
