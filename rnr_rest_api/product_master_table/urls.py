from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.show_all, name='show_all'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:pk>/', views.get_product, name='get_product'),
    path('products/update/<int:pk>/', views.update_product, name='update_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
]