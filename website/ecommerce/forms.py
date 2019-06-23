from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Required')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # def clean_email(self):
        #      email=self.cleaned_data.get('email')
        #
        #      try:
        #          User.objects.get(email=email)
        #      except User.DoesNotExist:
        #          return email
        #      raise forms.ValidationError("Email already exists")

