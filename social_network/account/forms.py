from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            self.add_error('password2', 'Пароли должны совпадать')
            raise forms.ValidationError('Пароли должны совпадать')
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            self.add_error('email','Пользователь с таким email уже существует')
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return cd['email']

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')




class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday', 'photo']