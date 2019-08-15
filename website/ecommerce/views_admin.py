from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views import View,generic
from django.contrib import messages
from .forms import AdminLoginForm , Add_Category,Sub_category,Features_Form
from . import forms
from .models import *


class AdminLoginView(generic.ListView):
    form_admin= forms.AdminLoginForm()
    template = 'ecommerce/admin_login.html'
    model = User

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect('admin_main')
        return super(AdminLoginView, self).dispatch(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        form = self.form_admin
        return render(self.request,self.template,{'form':form})

    def post(self,request,*args,**kwargs):
        form = forms.AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(self.request,user)
                return redirect('admin_main')
            else:
                messages.error(self.request,"Invalid username or password")
                return redirect("admin_login")
        return render(request, self.template_name, {'form': form})

class Logout(View):

    def get(self,request,*args,**kwargs):
        auth.logout(request)
        return render(request,'ecommerce/admin_login.html',{'message':"You are logout successfully!!"})


class Category_View(View):
      form = Add_Category()

      def dispatch(self, request, *args, **kwargs):
          if not request.user.is_superuser:
              return redirect('admin_login')
          return super(Category_View, self).dispatch(request, *args, **kwargs)

      def post(self,request,*args,**kwargs):
          form = Add_Category(request.POST)
          print("1")
          if form.is_valid():
              print("2")
              form.save()
              return render(request,'ecommerce/admin-category.html',{'form':form})
          else :
              return render(request,'ecommerce/admin-category.html',{'message':"error"})

      def get(self,request,*args,**kwargs):
          form = Add_Category()
          return render(request,'ecommerce/admin-category.html',{'form':form})

class Admin_page(View):

      def get(self,request,*args,**kwargs):
          return render(request ,'ecommerce/admin_main.html')

class Add_Subcategory(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('admin_login')
        return super(Add_Subcategory, self).dispatch(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        form = Sub_category(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'ecommerce/admin_main.html',{'form':form})
        else :
            return render(request,'ecommerce/admin_subcategory.html',{'message':"error"})


    def get(self,request,*args,**kwargs):
        form = Sub_category()
        return render(request,'ecommerce/admin_subcategory.html',{'form':form})

class Add_Features(View):
    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect('admin_login')
        return super(Add_Features,self).dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        form = Features_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'ecommerce/admin_main.html',{'form':form,'message':'saved successfully'})
        else :
            return render(request,'ecommerce/admin_features',{'form':form})

    def get(self,request,*args,**kwargs):
        form = Features_Form()
        return render(request,'ecommerce/admin_features.html',{'form':form})



