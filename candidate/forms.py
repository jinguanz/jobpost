__author__ = 'jinguangzhou'
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CandidateUser


class CandidateUserCreationUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = CandidateUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(CandidateUserCreationUserForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return cleaned_data

    def save(self, commit=True):
        user = super(CandidateUserCreationUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
