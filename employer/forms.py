__author__ = 'jinguangzhou'
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django import forms

from .models import EmployerUser


class EmployerUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
    company_name = forms.CharField(label='Company Name')

    class Meta:
        model = EmployerUser
        fields = ('email', 'company_name', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(EmployerUserCreationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return cleaned_data

    def save(self, commit=True):
        user = super(EmployerUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class EmployerUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = EmployerUser
        fields = ('email', 'company_name', 'is_active', 'last_login')
