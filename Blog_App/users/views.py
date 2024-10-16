"""
This module contains the views for user registration.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.


def register(request):
    """
    Register a new user.

    If the request method is POST, validate the user creation form and save the user.
    If the form is valid, redirect to the 'index' page.
    If the request method is GET, render the user creation form.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is POST and the form is valid, an HTTP redirect response to the
        'index' page.
        If the request method is GET, an HTTP response with the user creation form rendered.

    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
