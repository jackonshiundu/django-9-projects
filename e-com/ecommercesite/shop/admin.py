from django.contrib import admin
from .models import Products,Orders
# Register your models here.

admin.site.site_header="E-Commerce Site"
admin.site.site_title="ABC Shopping"
admin.site.index_title="Manage ABC Shopping"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category='default')

    change_category_to_default.short_description="Default Category"
    list_display=('name','price','discount_price','category','description','image')
    search_fields=['name','category']
    actions=['change_category_to_default']
    fields=['category','price']
    list_editable=['category','discount_price']

class OrderAdmin(admin.ModelAdmin):
    list_display=('name','email','address','city','state','zip','total')

admin.site.register(Products,ProductAdmin)
admin.site.register(Orders,OrderAdmin)