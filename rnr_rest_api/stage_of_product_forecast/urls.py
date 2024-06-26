from django.urls import path
from . import views

urlpatterns = [
    path('product-forecast-stages/', views.get_product_forecast_stages, name='get_product_forecast_stages'),
    path('product-forecast-stages/create/', views.create_product_forecast_stage, name='create_product_forecast_stage'),
    path('product-forecast-stages/update/<int:pk>/', views.update_product_forecast_stage, name='update_product_forecast_stage'),
    path('product-forecast-stages/delete/<int:pk>/', views.delete_product_forecast_stage, name='delete_product_forecast_stage'),
]
