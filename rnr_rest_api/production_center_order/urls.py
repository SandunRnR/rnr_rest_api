from django.urls import path
from . import views

urlpatterns = [
    path('centers/', views.show_all_centers, name='show_all_centers'),
    path('centers/create/', views.create_center, name='create_center'),
    path('centers/<int:pk>/', views.get_center, name='get_center'),
    path('centers/update/<int:pk>/', views.update_center, name='update_center'),
    path('centers/delete/<int:pk>/', views.delete_center, name='delete_center'),
]
