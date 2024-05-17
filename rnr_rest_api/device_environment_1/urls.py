from django.urls import path
from . import views

urlpatterns = [
    path('device-1-list/',views.ShowAll,name='device-1-list'),
    path('save-device-1/',views.SaveDevice,name='save-device-1'),
    path('delete-device-1/<int:id>',views.DeleteDevice,name='delete-device-1'),
    path('update-device-1/',views.UpdateDevice,name='update-device-1'),
]
