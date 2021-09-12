from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from ..constants import AuthenticationFields, General, Style


class EmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                Style.PLACEHOLDER: "Email",
                General.CLASS: "form-control"
            }
        ))


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                Style.PLACEHOLDER: "Email",
                General.CLASS: "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                Style.PLACEHOLDER: "Password",
                General.CLASS: "form-control"
            }
        ))


class PasswordConfirmForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                Style.PLACEHOLDER: "Password",
                General.CLASS: "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                Style.PLACEHOLDER: "Password check",
                General.CLASS: "form-control"
            }
        ))

    class Meta:
        model = User
        fields = (AuthenticationFields.PASSWORD1, AuthenticationFields.PASSWORD2)
