from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
import random
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            subject = 'Your Ecommerce OTP is here'
            otp = random.randint(999,9999)
            otp_key = Otp_Generate.objects.create(user=user,otp=otp)
            otp_key.save()

            message = render_to_string('ecommerce/otp_active.html', {

                'user': user,
                'otp':otp_key.otp
            })
            from_mail = EMAIL_HOST_USER
            to_mail = [user.email]
            send_mail(subject, message, from_mail, to_mail, fail_silently=False)
            #messages.success(request, 'Confirm your email to complete registering with ONLINE-AUCTION.')
            #return render(request,'ecommerce/otp_enter.html',{'form':form})
            context = {'id': user.id}
            print(context)
            return render(request ,'ecommerce/otp_enter.html' ,context)
        else:
            return render(request, 'ecommerce/signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect('otp_verify')
        # else:
        form = SignupForm()

        return render(request, 'ecommerce/signup.html', {'form': form})





class Home(View):

    def get(self,request,*args,**kwargs):
        context ={'Product': Product.objects.order_by('id')}
        print(context)
        return render(request , 'ecommerce/home.html',context)


class Activate_Otp(View):
    form = Otp_Verify()
    def post(self,request,id,*args,**kwargs):
        form = Otp_Verify(request.POST)
        print(id)
        context={'id':id}

        if form.is_valid():
            print("1")
            value = request.POST["otp_entered"]
            print(type(value))
            user1 = User.objects.filter(id=id)[0]
            print(user1)
            otp_key = Otp_Generate.objects.filter(otp=value,user=user1)
            if(otp_key):
                user1.is_active = True
                user1.save()
                login(request,user1)
                otp_key.delete()
                return redirect('home')
            else :

                return render(request,'ecommerce/otp_enter.html' ,context)
        else :
            return render(request ,'ecommerce/otp_enter.html' ,context)


    def get(self,request, *args,**kwargs):
        form = Otp_Verify()
        return render(request,'ecommerce/otp_enter.html',{'form':form})

class Login(View):
    form = LoginForm()
    def post(self ,request ,*args ,**kwargs):
        username = request.POST['username']
        password = request.POST['password']
        # username =forms.cleaned_data.get('username')
        # password = forms.cleaned_data.get('password')
        user = authenticate(username =username ,password =password)
        if user is not None:
            if user.is_active:
                login(request ,user)
                return redirect('home')
            else :
                return HttpResponse('Please Verify Your Otp first')
        else :
            messages.error(request ,'Incorrect Username or Password')
            return redirect('login')

    def get(self, request, *args, **kwagrs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = LoginForm()
        return render(request, 'ecommerce/login.html', {'form': form})


class Logout(View):

    def get(self ,request ,*args ,**kwargs):
        logout(request)
        return redirect('home')


class Product_detailView(View):

    def get(self,request,id,*args,**kwargs):
        print(id)
        context = {'detail':Product.objects.filter(id=id),}
        return render(request, 'ecommerce/product_detail.html',context)

class show_genres(View):

    def get(self,request,*args,**kwargs):
        return render(request,'ecommerce/category_detail.html', {'genres': Category.objects.all()})
