from django import forms
from testapp.models import EmployeeRegistration


class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = EmployeeRegistration
        fields = '__all__'
