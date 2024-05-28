from django.urls import path
from . import views

urlpatterns = [

    path('create-forecasting/', views.CreateForecasting, name='create-device-update'),

]



