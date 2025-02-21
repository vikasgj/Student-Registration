from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = Student
        fields = ['first_name','last_name','phone_number','email','date_of_birth']