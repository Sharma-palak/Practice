
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *

admin.site.register(Otp_Generate)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Product_Detail)
admin.site.register(Filters)
admin.site.register(Filter_Features)


