from django.urls import path
from . import views

urlpatterns = [
    path('colors/', views.show_all_colors, name='show_all_colors'),
    path('colors/create/', views.create_color, name='create_color'),
    path('colors/<int:pk>/', views.get_color, name='get_color'),
    path('colors/update/<int:pk>/', views.update_color, name='update_color'),
    path('colors/delete/<int:pk>/', views.delete_color, name='delete_color'),
]