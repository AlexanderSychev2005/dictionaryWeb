from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from users.models import CustomUser
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['email', 'password']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-input'})}
        help_texts = {
            'email': 'Your email must contain @.',
        }

    def clean_email(self):
        """
        Custom validation to check for unique email addresses.
        """
        email = self.cleaned_data['email']
        print(email)
        print(CustomUser.objects.filter(email=email).exists())
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email address already exists. Please choose a different one.")
        return email
