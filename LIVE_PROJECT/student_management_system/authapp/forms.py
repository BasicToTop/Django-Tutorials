from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, )
    password = forms.CharField()
    # password_confirmation = forms.CharField()


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField()
