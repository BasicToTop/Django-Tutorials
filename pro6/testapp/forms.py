from django import forms
from django.core import validators


def email_validator(value):
    email_extention = 'basictotop.in'
    # test@gmail.com
    splited_email = value.split('@')  # ['test', 'gmail.com']
    print('splited_email')
    if email_extention not in splited_email:
        raise forms.ValidationError('only basictotop.in mail can allowed here')
    else:
        return value


class ContactUsForm(forms.Form):
    GENDER_CHOICE = (
        ('', '------SELECT-----'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    name = forms.CharField(max_length=5, validators=[
                           validators.MinLengthValidator(2)])
    email = forms.EmailField(max_length=50, validators=[email_validator])
    phone_number = forms.CharField(max_length=15)
    gender = forms.ChoiceField(choices=GENDER_CHOICE)
    message = forms.CharField(widget=forms.Textarea, validators=[
                              validators.MaxLengthValidator(10),
                              validators.MinLengthValidator(5)])
    # dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # form validation by using clean method

    # def clean_name(self):
    #     name = self.cleaned_data['name']

    #     if len(name) <= 1:
    #         raise forms.ValidationError('Name must be more that 1 character')
    #     return name

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError(
                'Phone number must be digits only and it must be 10 digits')
        return phone_number
