from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
