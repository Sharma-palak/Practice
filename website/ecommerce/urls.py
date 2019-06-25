from django.conf.urls import url
from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$',views.Home.as_view(),name='home'),
    re_path(r'^signup/$',views.SignUp.as_view(),name='signup'),
    #re_path(r'^otp_verify/$' , views.Activate_Otp.as_view(), name='otp_verify')
    re_path(r'^otp_verify/(?P<id>[0-9]+)/$', views.Activate_Otp.as_view() ,name='otp_verify'),
    re_path(r'^login/$' ,views.Login.as_view() ,name ='login'),
    re_path(r'^logout/$' ,views.Logout.as_view() , name ='logout'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

