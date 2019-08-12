
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *

class Add_Category(admin.ModelAdmin):
    search_fields=['category']
    list_display =('name','slug',)
    class Meta:
        model=Category



admin.site.register(Otp_Generate)
admin.site.register(Product)
admin.site.register(Category,Add_Category)
admin.site.register(Product_Detail)
admin.site.register(Filters)
admin.site.register(Filter_Features)


