from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
import random
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate,logout
#from .tokens import account_activation_token
from django.core.mail import send_mail
from website.settings import EMAIL_HOST_USER
from django.views import View
from .forms import *

class SignUp(View):
    form = SignupForm()

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        print("2")

        if form.is_valid():
            print("1")
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            subject = 'Your Ecommerce OTP is here'
            otp = random.randint(999,9999)
            otp_key = Otp_Generate.objects.create(user=user,otp=otp)
            otp_key.save()
            print(otp_key)
            message = render_to_string('ecommerce/otp_active.html', {

                'user': user,
                'otp':otp_key.otp
            })
            from_mail = EMAIL_HOST_USER
            to_mail = [user.email]
            send_mail(subject, message, from_mail, to_mail, fail_silently=False)
            messages.success(request, 'Confirm your email to complete registering with ONLINE-AUCTION.')
            return redirect('home')
        else:
            return render(request, 'ecommerce/signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = SignupForm()

            return render(request, 'ecommerce/signup.html', {'form': form})





class Home(View):

    def get(self,request,*args,**kwargs):
       return render(request , 'ecommerce/home.html')

