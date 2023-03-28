from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True
                                )
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control '})
        self.fields['password2'].widget.attrs.update({'class': 'form-control '})
        self.fields['username'].widget.attrs.update({'class': 'form-control '})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control '})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control '})
        self.fields['email'].widget.attrs.update({'class': 'form-control '})


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Ім'я користувача",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
