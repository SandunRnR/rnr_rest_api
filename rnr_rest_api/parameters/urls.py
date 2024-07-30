from django.urls import path
from . import views

urlpatterns = [
    path('service-list/', views.show_all, name='service-list'),
    path('save-service/', views.save_service, name='save-service'),
    path('delete-service/<int:id>/', views.delete_service, name='delete-service'),
    path('update-service/<int:id>/', views.update_service, name='update-service'),
]