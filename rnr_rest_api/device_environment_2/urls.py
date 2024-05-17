from django.urls import path
from . import views

urlpatterns = [
    path('device-2-list/',views.ShowAll,name='device-2-list'),
    path('save-device-2/',views.SaveDevice,name='save-device-2'),
    path('delete-device-2/<int:id>',views.DeleteDevice,name='delete-device-2'),
    path('update-device-2/',views.UpdateDevice,name='update-device-2'),
]
