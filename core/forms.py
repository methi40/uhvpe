from django.forms import ModelForm
from django import forms
from captcha.fields import CaptchaField
from .models import WorkshopRegistration, EventRegistration


class WorkshopRegistrationForm(ModelForm):
    captcha = CaptchaField()
    def __init__(self, *args, **kwargs):
        super(WorkshopRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(
            max_length=50, required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'name',
                       'class': 'form-control',
                       'id': 'Name',
                       'placeholder': 'Enter Name',
                       'onblur': ''}
            )
        )

        self.fields['email'] = forms.EmailField(
            max_length=50, required=True,
            widget=forms.EmailInput(
                attrs={'type': 'email',
                       'name': 'email',
                       'class': 'form-control',
                       'id': 'Email',
                       'placeholder': 'Enter Email'}
            )
        )

        self.fields['phone'] = forms.IntegerField(
            required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'phone',
                       'class': 'form-control',
                       'id': 'phone',
                       'placeholder': 'Enter Phone No',
                       'onblur': ''
                       }
            )
        )

    def clean(self):
        cleaned_data = super(WorkshopRegistrationForm, self).clean()
        return cleaned_data
    class Meta:
        model = WorkshopRegistration
        fields = ['name','email','phone']


class EventRegistrationForm(ModelForm):
    captcha = CaptchaField()
    def __init__(self, *args, **kwargs):
        super(WorkshopRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(
            max_length=50, required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'name',
                       'class': 'form-control',
                       'id': 'Name',
                       'placeholder': 'Enter Name',
                       'onblur': ''}
            )
        )

        self.fields['email'] = forms.EmailField(
            max_length=50, required=True,
            widget=forms.EmailInput(
                attrs={'type': 'email',
                       'name': 'email',
                       'class': 'form-control',
                       'id': 'Email',
                       'placeholder': 'Enter Email'}
            )
        )

        self.fields['phone'] = forms.IntegerField(
            required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'phone',
                       'class': 'form-control',
                       'id': 'phone',
                       'placeholder': 'Enter Phone No',
                       'onblur': ''
                       }
            )
        )

    def clean(self):
        cleaned_data = super(WorkshopRegistrationForm, self).clean()
        return cleaned_data
    class Meta:
        model = WorkshopRegistration
        fields = ['name','email','phone']