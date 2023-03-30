
from django.urls import path, re_path,include

urlpatterns = [
        path('mediaapp/',include('mediaapp.urls')),

]
