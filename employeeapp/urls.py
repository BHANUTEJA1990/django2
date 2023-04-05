from django.urls import path


from .import views
urlpatterns=[

                path('add_employee/',views.add_employee,name='add_employeee'),
                path('show_employee',views.show_employee,name='show_employee'),
                path('del_employee/<int:id>',views.del_employee,name='del_employee'),
                path('update_employee/<int:id>',views.update_employee,name='update_employee'),
]