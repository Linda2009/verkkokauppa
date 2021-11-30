from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
from .models import (Category,Product,)




#_____________________________ CategoryAdmin_______________________________
class CategoryAdmin(admin.ModelAdmin):
        search_fields = ['name']
        readonly_fields = ('my_image_tag',)
        list_display=['title','status','my_image_tag']
        list_filter=['status','create_at']



admin.site.register(Category,MPTTModelAdmin)
admin.site.register(models.Product)