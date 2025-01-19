from django.contrib import admin
from .models import Product, Customer, Sale, Bill, Category


class Product_Manager(admin.ModelAdmin):
    list_display=['name','price','quantity', 'add_date']


class Customer_Manager(admin.ModelAdmin):
    list_display=['name']


class Sale_Manager(admin.ModelAdmin):
    list_display=['customer','quantity','total_amount','sale_date']


class Bill_Manager(admin.ModelAdmin):
    list_display=['customer','quantity', 'sale_date']


class Category_Manager(admin.ModelAdmin):
    list_display=['name']



admin.site.register(Product, Product_Manager)
admin.site.register(Customer, Customer_Manager)
admin.site.register(Sale, Sale_Manager)
admin.site.register(Bill, Bill_Manager)
admin.site.register(Category, Category_Manager)
