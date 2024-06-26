from django.urls import path
from . import views

urlpatterns = [
    path('material-list/',views.ShowAll, name= 'material-list'),
    path('material-create/',views.CreateProduct,name='material-create'),
    # path('material-delete/<int:id>/', views.DeleteProduct, name='material-delete'),
    # path('material-update/', views.UpdateProduct, name='material-update'),
    path('material-update/<int:id>/', views.UpdateProduct, name='material-update'),  # Updated URL pattern
    path('material-delete/<int:id>/', views.DeleteProduct, name='material-delete'),
    path('material-detail/<int:id>/', views.GetProductById, name='material-detail'),  # New URL pattern

]