from django.conf.urls import url
from django.urls import path, re_path
from . import views_admin
from django.contrib.auth import views as built_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     re_path(r'^add_category/$',views_admin.Category_View.as_view(),name='add'),
     re_path(r'^login/$',views_admin.AdminLoginView.as_view(),name='login'),
     re_path(r'^main/$',views_admin.Admin_page.as_view(),name='admin_main'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

