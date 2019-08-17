from django.conf.urls import url
from django.urls import path, re_path
from . import views_admin
from django.contrib.auth import views as built_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     re_path(r'^add_category/$',views_admin.Category_View.as_view(),name='add'),
     re_path(r'^add_subcategory/$',views_admin.Add_Subcategory.as_view(),name='add_subcategory'),
     re_path(r'^$',views_admin.AdminLoginView.as_view(),name='admin_login'),
     re_path(r'^main/$',views_admin.Admin_page.as_view(),name='admin_main'),
     re_path(r'^logout/$',views_admin.Logout.as_view(),{'next_page': 'admin_login'},name='admin_logout'),
     re_path(r'^add_features/$',views_admin.Add_Features.as_view(),name='admin_features'),
     re_path(r'^add_options/$',views_admin.Add_Options.as_view(),name='add_options'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


