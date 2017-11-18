from django.forms import ModelForm
from django import forms
from .models import WorkshopRegistration


class WorkshopRegistrationForm(ModelForm):
    name = forms.CharField(label='Name', max_length=50, required=True)
    email = forms.EmailField(label='Email', required=True)
    phone = forms.IntegerField(label='Phone Number', required=True)
    class Meta:
        model = WorkshopRegistration
        fields = ['name','email','phone']
