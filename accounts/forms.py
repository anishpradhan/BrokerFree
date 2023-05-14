from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone_number = forms.CharField(max_length=20, required=False, help_text='Optional.')
    class Meta:
        model = get_user_model()
        fields = ('full_name', 'email', 'username', 'phone_number', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')