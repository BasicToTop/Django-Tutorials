from django import forms
from mainapp.models import Country, State, Qualification, Gender, University, Student


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['state_code', 'state_name', 'country_name', 'description']
        # fields = '__all__'


class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'


class GenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = '__all__'


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
