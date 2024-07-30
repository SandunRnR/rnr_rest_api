from django.urls import path
from . import views

urlpatterns = [
    path('styles/', views.show_all_styles, name='style-list'),
    path('styles/create/', views.create_style, name='style-create'),
    path('styles/<int:pk>/', views.get_style, name='style-detail'),
    path('styles/update/<int:pk>/', views.update_style, name='style-update'),
    path('styles/delete/<int:pk>/', views.delete_style, name='style-delete'),
]