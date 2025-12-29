from django.urls import path
from testapp import views

urlpatterns = [
    path('employee-registration/', views.employee_registration,
         name='employee_registration')
]
