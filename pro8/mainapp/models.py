from django.db import models

# Create your models here.
# from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name
