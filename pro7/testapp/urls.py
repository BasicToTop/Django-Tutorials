from django.urls import path
from .views import employee_list, EmployeeRegistration

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/register/', EmployeeRegistration.as_view(), name='employee_registration'),
]