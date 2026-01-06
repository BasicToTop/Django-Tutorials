from django.urls import path
from testapp import views

urlpatterns = [
    path('employee-registration/', views.employee_registration,
         name='employee_registration'),
    path('contact-info/', views.contact_info_create, name='contact_info_create')
]
