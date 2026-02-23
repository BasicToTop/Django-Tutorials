from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name', required=False)
    # middle_name = forms.CharField(max_length=30, required=False, label='Middle Name')
    # last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(label='Email Address', required=False)
    # phone_number = forms.CharField(max_length=15, label='Phone Number')
    # position = forms.CharField(max_length=50, label='Position')
    # doj = forms.DateField(label='Date of Joining', widget=forms.SelectDateWidget)
    salary = forms.FloatField(label='Salary', required=False)
    # is_active = forms.BooleanField(required=False, initial=True, label='Is Active')
    from_salary = forms.FloatField(label='From Salary', required=False)
    to_salary = forms.FloatField(label='To Salary', required=False)



class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'