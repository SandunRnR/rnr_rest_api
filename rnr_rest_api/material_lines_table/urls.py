from django.urls import path
from . import views

urlpatterns = [
    path('material-list/',views.ShowAll, name= 'material-list'),
    path('material-create/',views.CreateProduct,name='material-create'),
    path('material-delete/<int:id>/', views.DeleteProduct, name='material-delete'),
    path('material-update/', views.UpdateProduct, name='material-update'),

]