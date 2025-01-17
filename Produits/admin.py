from django.contrib import admin
from .models import Product, Customer, Sale, Bill


class Product_Manager(admin.ModelAdmin):
    list_display=['name','price','quantity', 'add_date']


class Customer_Manager(admin.ModelAdmin):
    list_display=['name']


class Sale_Manager(admin.ModelAdmin):
    list_display=['customer','quantity','total_amount','sale_date']


class Bill_Manager(admin.ModelAdmin):
    list_display=['customer','price','quantity', 'add_date']



admin.site.register(Product, Product_Manager)
admin.site.register(Customer, Customer_Manager)
admin.site.register(Sale, Sale_Manager)
admin.site.register(Bill, Bill_Manager)
