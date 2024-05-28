from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name='apiOverview'),

    path('create-device-update/', views.CreateDeviceUpdate, name='create-device-update'),
    path('get-all-updated-devices/',views.ShowAll, name = 'get-all-updated-devices'),
    path('delete-updated-device/<int:id>',views.DeleteUpdatedDevice,name='delete-updated-device'),
    path('update-updated-device/',views.UpdateUpdatedDevice,name='update-updated-device'),

]
