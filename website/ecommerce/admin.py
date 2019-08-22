
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *

class Add_Category(admin.ModelAdmin):
    search_fields=['category']
    list_display =('name','slug',)
    class Meta:
        model=Category

class Filter_Admin(admin.ModelAdmin):
   # search_fields=['category']
    list_display=('name_feature','categoryss')
    class Meta:
        model = Filters


    def categoryss(self, obj):
        return "\n".join([p.name for p in obj.category.all()])

class Option_admin(admin.ModelAdmin):
    list_display =['name']
    class Meta:
        model = Filter_options

admin.site.register(Otp_Generate)
admin.site.register(Product)
admin.site.register(Category,Add_Category)
admin.site.register(Product_Detail)
admin.site.register(Filters,Filter_Admin)
admin.site.register(Filter_options,Option_admin)



