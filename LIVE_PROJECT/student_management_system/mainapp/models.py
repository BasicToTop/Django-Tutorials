from django.db import models

# Create your models here.


class Country(models.Model):
    '''
    Docstring for Country
    This models is responsible to handling the all countries
    '''
    country_code = models.CharField(max_length=5, unique=True)
    country_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)


class State(models.Model):
    '''
    Docstring for State,
    State models is responsible to handling the all kinds of states
    '''
    state_code = models.CharField(max_length=5, unique=True)
    state_name = models.CharField(max_length=50, unique=True)
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)


class Qualification(models.Model):
    '''
    Docstring for Qualification,
    Qualification models is responsible to handling the all kinds of Qualification
    '''
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)


class Gender(models.Model):
    '''
    Docstring for Gender,
    Gender models is responsible to handling the all kinds of Gender
    '''
    name = models.CharField(max_length=15, unique=True)
    description = models.TextField(null=True, blank=True)


class University(models.Model):
    '''
    Docstring for University,
    University models is responsible to handling the all kinds of University
    '''
    uc_id = models.CharField(max_length=10, primary_key=True)
    uc_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    founded_by = models.CharField(max_length=100)
    founded_year = models.DateField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Student(models.Model):
    '''
    Docstring for Student,
    Student models is responsible to handling the all kinds of Student
    '''
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    rollno = models.CharField(max_length=50, unique=True)
    university_college_name = models.ForeignKey(
        University, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    dob = models.DateField()
    Gender = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
