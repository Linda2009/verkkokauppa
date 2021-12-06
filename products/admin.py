from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
from .models import (Category,Product,)
from mptt.admin import  DraggableMPTTAdmin



#_____________________________ CategoryAdminI_______________________________
# class CategoryAdminI(admin.ModelAdmin):
#         search_fields = ['name']
#         readonly_fields = ('Cat_image_disp',)
#         list_display=['name', 'Cat_image_disp',]
#         list_filter=['create_at']

# admin.site.register(Category,CategoryAdminI)

#_____________________________ CategoryAdminII_______________________________

class CategoryAdminII(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',)
    list_display_links = ('indented_title',)
   
admin.site.register(Category,CategoryAdminII)



class ProductAdminI(admin.ModelAdmin):
   
    list_display=['Prod_image','product_code','name','category','cost','regular_price','discounted_price','discount_percent']
 
    # readonly_fields = ('cost','discounted_price')
#     @property
#     def auto_cost(self):
#         auto_cost = super().auto_cost
#         auto_cost._js.append('product/js/auto_cost.js')
#         return auto_cost

admin.site.register(Product,ProductAdminI)
