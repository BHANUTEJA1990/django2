from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('validapp/',include('validapp.urls')),
    path('studentrelapp/',include('studentrelapp.urls')),
    path('productapp/',include('productapp.urls')),
    path('employeeapp/',include('employeeapp.urls')),
]
