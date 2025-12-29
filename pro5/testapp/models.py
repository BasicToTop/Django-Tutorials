from django.db import models

# Create your models here.


class EmployeeRegistration(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True, null=True, blank=False)
    phone_number = models.IntegerField(unique=True, null=False, blank=True)
    address = models.TextField(null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    doj = models.DateField(null=False, blank=False)
    adhaar = models.CharField(max_length=16, unique=True)
