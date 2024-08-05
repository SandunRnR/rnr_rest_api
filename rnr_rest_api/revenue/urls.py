from django.urls import path
from . import views

urlpatterns = [
    path('revenues/', views.show_all_revenues, name='show_all_revenues'),
    path('revenue/create/', views.create_revenue, name='create_revenue'),
    path('revenue/<int:pk>/', views.get_revenue, name='get_revenue'),
    path('revenue/update/<int:pk>/', views.update_revenue, name='update_revenue'),
    path('revenue/delete/<int:pk>/', views.delete_revenue, name='delete_revenue'),
]
