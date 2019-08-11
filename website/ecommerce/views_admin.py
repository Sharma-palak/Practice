from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views import View,generic
from django.contrib import messages
from .forms import AdminLoginForm , Add_Category
from . import forms

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


class Category_View(View):
      form = Add_Category()
      def post(self,request,*args,**kwargs):
          form = Add_Category(request.POST)
          if form.is_valid():
              return render(request,'ecommerce/admin-category.html',{'form':form})
          else :
              return render(request,'ecommerce/admin-category.html',{'message':"error"})

      def get(self,request,*args,**kwargs):
          form = Add_Category()
          return render(request,'ecommerce/admin-category.html',{'form':form})

class Admin_page(View):

      def get(self,request,*args,**kwargs):
          return render(request ,'ecommerce/admin_main.html')