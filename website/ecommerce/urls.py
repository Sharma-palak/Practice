from django.conf.urls import url
from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$',views.Home.as_view(),name='home'),
    re_path(r'^signup/$',views.SignUp.as_view(),name='signup'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)