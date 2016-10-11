from django import forms


class RegistrationForm(forms.Form):
    login = forms.CharField(label='Login', min_length=2, max_length=30, required=True)
    password = forms.CharField(label='Password', min_length=2, max_length=30, required=True, widget=forms.PasswordInput())
