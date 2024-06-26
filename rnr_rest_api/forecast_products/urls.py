from django.urls import path
from . import views

urlpatterns = [
    path('',views.productsOverview,name='productsOverview'),
    path('product-list/',views.ShowAll,name='product-list'),
    path('product-create/',views.CreateProduct,name='product-create'),
    path('product-delete/<int:id>/', views.DeleteProduct, name='product-delete'),
    # path('product-update/', views.UpdateProduct, name='product-update'),
    path('product-update/<int:id>/', views.UpdateProduct, name='product-update'),
    path('product-detail/<str:product_id>/', views.ProductDetail, name='product-detail'),

]
