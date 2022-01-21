from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'