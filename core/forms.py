from django.forms import ModelForm
from django import forms
from .models import WorkshopRegistration, EventRegistration
from recaptcha2.fields import  ReCaptchaField
from recaptcha2.fields import ReCaptchaWidget

class WorkshopRegistrationForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget(explicit=True,callback='enableButton'),label='')

    def __init__(self, *args, **kwargs):
        super(WorkshopRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(
            max_length=50, required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'name',
                       'class': 'form-control',
                       'id': 'Name',
                       'placeholder': 'Enter Name*',
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
                       'placeholder': 'Enter Email*'}
            )
        )

        self.fields['phone'] = forms.IntegerField(
            required=True,
            widget=forms.TextInput(
                attrs={'type': 'text',
                       'name': 'phone',
                       'class': 'form-control',
                       'id': 'phone',
                       'pattern':'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$',
                       'title':'eg. 9454301987',
                       'placeholder': 'Enter Phone No*',
                       'onblur': ''
                       }
            )
        )

    def clean(self):
        cleaned_data = super(WorkshopRegistrationForm, self).clean()
        return cleaned_data

    class Meta:
        model = WorkshopRegistration
        fields = ['name', 'email', 'phone']


class EventRegistrationForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget(explicit=True, callback='enableButton'), label='')

    def __init__(self, *args, **kwargs):
        super(EventRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label='Name*',
                                              max_length=50, required=True,
                                              widget=forms.TextInput(
                                                  attrs={'type': 'text',
                                                         'name': 'name',
                                                         'class': 'form-control',
                                                         'id': 'Name',
                                                         'placeholder': 'Enter Name'}
                                              )
                                              )

        self.fields['email'] = forms.EmailField(label='Email*',
                                                max_length=50, required=True,
                                                widget=forms.EmailInput(
                                                    attrs={'type': 'email',
                                                           'name': 'email',
                                                           'class': 'form-control',
                                                           'id': 'Email',
                                                           'placeholder': 'Enter Email'}
                                                )
                                                )

        self.fields['phone'] = forms.IntegerField(label='Phone*',
                                                  required=True,
                                                  widget=forms.TextInput(
                                                      attrs={'type': 'text',
                                                             'name': 'phone',
                                                             'class': 'form-control',
                                                             'id': 'phone',
                                                             'pattern': '^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$',
                                                             'title': 'eg. 9454301987',
                                                             'placeholder': 'Enter Phone No*'
                                                             }
                                                  )
                                                  )
        self.fields['student_no'] = forms.CharField(label='Student No.',
                                                    required=False,
                                                    widget=forms.TextInput(
                                                        attrs={'type': 'text',
                                                               'placeholder': 'Enter Student no.',
                                                               'name': 'student_no',
                                                               'class': 'form-control',
                                                               'title': 'eg. 1510109',
                                                               'id': 'student_no',
                                                               'pattern': '^[0-9]{7}[dmlDML]?$'
                                                               }
                                                    )
                                                    )
        self.fields['branch'] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                  choices=((None, '----'),
                                                           ('MCA', 'MCA'), ('MBA', 'MBA'), ('CS', 'CS'), ('IT', 'IT'),
                                                           ('ECE', 'ECE'), ('EN', 'EN'), ('ME', 'ME'), ('EI', 'EI'),
                                                           ('CE', 'CE'),),
                                                  required=False

                                                  )

        self.fields['year'] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                choices=((0, '----'), (1, '1'), (2, '2'), (3, '3'), (4, '4')),
                                                required=False)

    def clean(self):
        cleaned_data = super(EventRegistrationForm, self).clean()
        return cleaned_data

    class Meta:
        model = EventRegistration
        fields = ['name', 'email', 'phone', 'student_no', 'branch', 'year']


