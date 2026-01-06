from django import forms
from testapp.models import EmployeeRegistration


class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = EmployeeRegistration
        fields = '__all__'


class ContactInformationForm(forms.Form):
    full_name = forms.CharField()
    phone_number = forms.CharField()
    email_address = forms.EmailField()

    def clean_full_name(self):
        print('Form validating -- Full Name validation is started..')
        get_full_name = self.cleaned_data['full_name']
        print('get_full_name ', get_full_name)
        if len(get_full_name) < 2:
            error_message = "Invalid full name alteast length must be 2 characters"
            raise forms.ValidationError(error_message)
        return get_full_name
