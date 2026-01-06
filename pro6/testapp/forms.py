from django import forms


class ContactUsForm(forms.Form):
    GENDER_CHOICE = (
        ('', '------SELECT-----'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    gender = forms.ChoiceField(choices=GENDER_CHOICE)

    # form validation by using clean method

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) <= 1:
            raise forms.ValidationError('Name must be more that 1 character')
        return name

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError(
                'Phone number must be digits only and it must be 10 digits')
        return phone_number
