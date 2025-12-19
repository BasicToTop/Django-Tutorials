# wokring with django forms
from django import forms


class StudentForm(forms.Form):
    # fields according to the model
    name = forms.CharField(max_length=100)
    rollno = forms.IntegerField()
    father_name = forms.CharField(max_length=100)
    mother_name = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=10)
    email = forms.EmailField()


"""
<label for="id_name">Name:</label>
<input type="text" name="name" maxlength="100" required id="id_name">

"""
