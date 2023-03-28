from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import LoginForm, SignUpForm


# Create your views here.

class SignUpView(CreateView):
    template_name = "authentication/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = "authentication/login.html"
    authentication_form = LoginForm
    next_page = 'home'


class CustomLogoutView(LogoutView):
    next_page = 'home'
