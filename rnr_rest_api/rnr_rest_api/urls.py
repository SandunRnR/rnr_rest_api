"""
URL configuration for rnr_rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('forecast_products.urls')),
    path('api/',include('object_detection.urls')),
    path('api/',include('device_environment_1.urls')),
    path('api/',include('device_environment_2.urls')),
    path('api/',include('device_state.urls')),
    path('api/',include('device_update.urls')),
    path('api/',include('material_lines_table.urls')),
    # path('api/', include('login.urls')),
    path('api/', include('log_in.urls')),
    path('api/', include('stage_of_product_forecast.urls')),
    # path('api/', include('data_capturing_system.urls')),
    path('api/', include('chat_app.urls')),
    path('api/', include('product_master_table.urls')),
    path('api/', include('size_group.urls')),
    path('api/', include('color_group.urls')),
    path('api/', include('style.urls')),
    path('api/', include('parameters.urls')),

]