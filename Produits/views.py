from django.shortcuts import render, redirect
from .models import *

def home(request) :
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})


def add_product(request):
    if(request.method=="POST"):
        name=request.POST['name']
        quantity=request.POST['quantity']
        price=request.POST['price']
        description=request.POST['description']
        expiration_date=request.POST['expiration_date']
        image=request.FILES['image']
        category=Category.objects.get(pk=request.POST['category'])

        save_data=Product(name=name,quantity=quantity,price=price,description=description,expiration_date=expiration_date, image=image, category=category)
        save_data.save()
        return redirect('home')
    else:
        category=Category.objects.all()
    return render(request,'form_add_product.html',{'category':category})


