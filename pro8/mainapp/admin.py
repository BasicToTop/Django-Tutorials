from django.contrib import admin
from mainapp.models import Employee
# Register your models here.

admin.site.register(Employee) 
# This line registers the Employee model with the Django admin site, 
# allowing you to manage Employee records through the admin interface.