from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class Authentication(AuthenticationForm):
    username = forms.CharField(max_length=255,widget=forms.TextInput(attrs = {
        'id' : "username",
    }))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs = {
        'id' : "password",
    }))
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class Regist(UserCreationForm):
    email = forms.EmailField(label= 'Email',max_length=255, widget=forms.TextInput(attrs={
        'id': "username",
    }))
    username = forms.CharField(label='Username',max_length=255,widget=forms.TextInput(attrs={
        'id': "username",
    }))
    password1 = forms.CharField(label= 'Password', max_length=32, widget=forms.PasswordInput(attrs={
        'id': "password",
    }))
    password2 = forms.CharField(label= 'Confirm password',max_length=32, widget=forms.PasswordInput(attrs={
        'id': "password",
    }))
    class Meta:
        model = get_user_model()
        fields = ['email','username', 'password1','password2']


    def clean_password2(self):
        print(self.cleaned_data['password1'], self.cleaned_data['password2'])
        if self.cleaned_data['password1'] == self.cleaned_data['password2']:
            #print(self.cleaned_data['password1'],self.cleaned_data['password2'])
            return self.cleaned_data['password2']
        raise forms.ValidationError('Passwords not equals')

    def clean_email(self):
        if not get_user_model().objects.filter(email = self.cleaned_data['email']).exists:
            raise forms.ValidationError('This Email already registrate')
        return self.cleaned_data['email']

    def clean_username(self):
        print(self.cleaned_data['username'])
        if not get_user_model().objects.filter(username = self.cleaned_data['username']).exists:
            print(get_user_model().objects.filter(username = self.cleaned_data['username']))
            raise forms.ValidationError('This username already exist. Please create new')
        return self.cleaned_data['username']

    def save(self, commit=True):
        user = get_user_model().objects.create(
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
        )
        user.set_password(self.cleaned_data['password2'])
        user.save()
        return user


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label= 'Enter your email address, which you had been used for registration',max_length=64)


    def clean_email(self):
        if not get_user_model().objects.filter(email = self.cleaned_data['email']).exists:
            raise forms.ValidationError('This email not registrate yet')
        return self.cleaned_data['email']

class ResetPasswordConfirmForm(forms.Form):
    password1 = forms.CharField(label= 'Type new password',max_length=64, widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirm password',max_length=64, widget=forms.PasswordInput)


    def clean_password2(self):
        if not self.cleaned_data['password1'] == self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords not equals')
        return self.cleaned_data['password2']

