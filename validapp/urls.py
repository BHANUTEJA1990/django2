from django.urls import path,re_path
from .import views
urlpatterns=[
    path('show_text/',views.show_text,name='show_text'),
    path('job/<action>', views.job, name='job'),
    path('get_job/<int:id>', views.get_job, name='get_job'),
]