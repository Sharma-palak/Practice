from django.conf.urls import url
from django.urls import path, re_path
from . import views_customer
from django.contrib.auth import views as built_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$',views_customer.Home.as_view(),name='home'),
    re_path(r'^signup/$',views_customer.SignUp.as_view(),name='signup'),
    #re_path(r'^otp_verify/$' , views.Activate_Otp.as_view(), name='otp_verify')
    re_path(r'^otp_verify/(?P<id>[0-9]+)/$', views_customer.Activate_Otp.as_view() ,name='otp_verify'),
    re_path(r'^login/$' ,views_customer.Login.as_view() ,name ='login'),
    re_path(r'^logout/$' ,views_customer.Logout.as_view() , name ='logout'),
    re_path(r'^detail/(?P<id>[0-9]+)/$',views_customer.Product_detailView.as_view() ,name ='detail'),
    re_path(r'^genres/$', views_customer.show_genres.as_view(),name='genres'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)