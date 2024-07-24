from django.urls import path
from . import views


urlpatterns = [
    path('sizes/', views.show_all_sizes, name='show_all_sizes'),
    path('sizes/create/', views.create_size, name='create_size'),
    path('sizes/<int:pk>/', views.get_size, name='get_size'),
    path('sizes/update/<int:pk>/', views.update_size, name='update_size'),
    path('sizes/delete/<int:pk>/', views.delete_size, name='delete_size'),
]