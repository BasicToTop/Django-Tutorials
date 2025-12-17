from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
