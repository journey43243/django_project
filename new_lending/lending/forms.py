from django import forms
from .models import Users


class Authentication(forms.Form):
    mail = forms.EmailField(max_length=255, widget= forms.EmailInput(attrs={'class' : 'form-control', 
                                                                            'id' : 'exampleInputEmail1',
                                                                            'aria-describedby' : 'emailHelp',
                                                                            'placeholder' : 'Enter email'}))
    password = forms.CharField(max_length=32, widget= forms.PasswordInput(attrs={
        'type' : 'password',
        'class' : 'form-control',
        'id' : 'exampleInputPassword1',
        'placeholder' : 'Password'
        }))
