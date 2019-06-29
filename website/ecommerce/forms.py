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


    def clean_email(self):
         email=self.cleaned_data.get('email')

         try:
             User.objects.get(email=email)
         except User.DoesNotExist:
             return email
         raise forms.ValidationError("Email already exists")

    def clean_username(self ,*args ,**kwargs):
        username =self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            print(username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Username is already taken")

    # def clean(self ,*args,**kwargs):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')
    #     username = cleaned_data.get('username')
    #     if(password1 !=password2):
    #          raise forms.ValidationError("The two passwords must be same ")
    #
    #     # if((password1.find(username)!= -1) or (username.find(password1)!=-1)):
    #     #     raise forms.ValidationError("Username andd password can have no similarity")
    #
    #     if(len(password1)<8):
    #         raise forms.ValidationError("Your password is too short")
    #
    #
    # def save(self):
    #     self.full_clean()
    #     super().save()




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


    def clean_username(self,*args,**kwargs):
         username = self.cleaned_data.get['username']
         print(username)
         key = User.objects.filter(username=username)
         if(not key):
             raise forms.ValidationError("Incorrect username")
         return username


    def clean_password(self,*args,**kwargs):
        password = self.cleaned_data.get['password']
        key = User.objects.filter(password=password)
        if(not key):
            raise forms.ValidationError("Incorrect password")
        return password

