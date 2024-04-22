from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {'email': forms.EmailInput()}
        help_texts = {
            'email': 'Your email must contain @.',
        }

    def clean_email(self):
        """
        Custom validation to check for unique email addresses.
        """
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email address already exists. Please choose a different one.")
        return email
