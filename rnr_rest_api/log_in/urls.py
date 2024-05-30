from django.urls import path
from . import views

urlpatterns = [
    path('log_in/', views.Login_User, name='login_in'),
]