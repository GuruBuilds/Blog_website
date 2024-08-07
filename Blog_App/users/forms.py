"""
This module contains the RegisterForm class for user registration.
"""

from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    """
    A custom form for user registration.

    This form extends the UserCreationForm provided by Django and adds an email field.
    It also overrides the __init__ method to remove the help text for certain fields.

    """
    email = forms.EmailField()

    class Meta:
        """
        Meta class for RegisterForm.
        Specifies the model and fields for the form.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        """
        Clean the email field.
        Check if the entered email already exists in the User model.
        If it does, raise a validation error.
        Returns:
            The cleaned email value.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the RegisterForm.
        Remove the help text for certain fields based on rules.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
