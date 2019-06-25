from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from .models import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Required')
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password1', 'password2']

        # def clean_email(self):
        #      email=self.cleaned_data.get('email')
        #
        #      try:
        #          User.objects.get(email=email)
        #      except User.DoesNotExist:
        #          return email
        #      raise forms.ValidationError("Email already exists")

class Otp_Verify(forms.ModelForm):
    otp_entered = forms.IntegerField()
    class Meta:
        model = User
        fields = ['otp_entered',]

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields =['username' ,'password']
