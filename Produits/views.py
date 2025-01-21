from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime
from django.views.generic import CreateView
from .forms import Add_product
from django.urls import reverse_lazy

def home(request) :
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})


# Generation des formulaires al'aide des classe generiques

class Add_products(CreateView):
    model = Product
    form_class = Add_product
    template_name = 'form_add_product.html'
    success_url = reverse_lazy('home')


# def add_product(request):
#     # Création de la variable pour la gestion des erreurs
#     errors = {}
#     category = Category.objects.all() 

#     if request.method == "POST":
#         name = request.POST['name']
#         quantity = request.POST['quantity']
#         price = request.POST['price']
#         description = request.POST['description']
#         expiration_date = request.POST['expiration_date']
#         image = request.FILES['image']

#         # Validation du prix
#         try:
#             price = float(price)
#             if price < 0:
#                 errors['price'] = "The price cannot be negative!"
#         except ValueError:
#             errors['price'] = "Please enter a number for the price!"

#         # Validation de la quantité
#         try:
#             quantity = float(quantity)
#             if quantity < 0:
#                 errors['quantity'] = "The quantity cannot be negative!"
#         except ValueError:
#             errors['quantity'] = "Please enter a number for the quantity!"

#         if not errors:
#             try:
#                 category_instance = Category.objects.get(pk=request.POST['category'])
#                 save_data = Product(
#                     name=name,
#                     quantity=quantity,
#                     price=price,
#                     description=description,
#                     expiration_date=expiration_date,
#                     image=image,
#                     category=category_instance
#                 )
#                 save_data.save()
#                 messages.success(request, "The Product has been successfully added!")
#                 return redirect('home')
#             except Category.DoesNotExist:
#                 errors['category'] = "The specified category does not exist!"
#             except KeyError as e:
#                 errors[str(e)] = f"The data {e} is missing!"
#             except Exception as e:
#                 messages.error(request, f"An error has occurred! {e}")

#     return render(request, 'form_add_product.html', {'category': category, 'errors': errors})