from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime
from django.views.generic import CreateView
from .forms import Add_product, Adding_sales
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'welcome.html')


@login_required(login_url='login')
def home(request) :
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})


# Generation des formulaires al'aide des classe generiques

class Add_products(LoginRequiredMixin,CreateView):
    model = Product
    form_class = Add_product
    template_name = 'form_add_product.html'
    success_url = reverse_lazy('home')


@login_required(login_url='login')
def update_product(request, id):
    product=get_object_or_404(Product, id=id)
    categories=Category.objects.all()
    errors={}

    if request.method=="POST" :
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        expiration_date = request.POST.get('expiration_date')
        image = request.FILES.get('image')

        if not name:
            errors['name']="The product name is mandatory"

        if not category_id:
            errors['category']="The product category is mandatory"

        if not quantity:
            errors['quantity']="The product quantity is mandatory"

        if not price:
            errors['price']="The product price is mandatory"

        if not expiration_date:
            errors['expiration_date']="The product expiration_date is mandatory"

        if not description:
            errors['description']="The product description is mandatory"

        if not errors:
            category=get_object_or_404(Category, id=category_id)
            product.name=name
            product.category=category
            product.price=price
            product.quantity=quantity
            product.description=description
            product.expiration_date=expiration_date
            
            if image:
                fs=FileSystemStorage()
                filename = fs.save(name, image)
                product.image=fs.url(filename)

        product.save()
        messages.success(request, "The product was updated successfully !")
        return redirect('home')
    
    else :
        for key, errrors in errors.items() :
            messages.ERROR(request, errors)

    return render(request, "update.html", {'product':product, 'categories':categories, 'errors':errors})



@login_required(login_url='login')
def delete_product(request,id):
    product = get_object_or_404(Product,id=id)
    product.delete()
    messages.success(request, "The product was successfully deleted !")
    return redirect('home')



def details_product(request, id):
    product = Product.objects.get(id=id) 
    return render(request, "details.html", {'product':product})


@login_required(login_url='login')
def search_product(request):
    query = request.GET.get("product")
    products = Product.objects.filter(name__icontains=query)
    context = {
        'products':products,
    }
    return render(request,"search.html", context)



# vente de produits

@login_required(login_url='login')
def sale(request, id):
    product = get_object_or_404(Product, id=id)
    message = None

    if request.method == "POST":
        form = Adding_sales(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            customer = form.cleaned_data['customer']

            if quantity > product.quantity:
                message = "La quantité demandée est supérieure à votre stock."
            else:
                customer, created = Customer.objects.get_or_create(name=customer)

                customer.save()

                total_amount = product.price * quantity

                sale = Sale(quantity=quantity, total_amount=total_amount, customer=customer, product=product)
                sale.save()

                product.quantity -= quantity
                product.save()  

                return redirect('billing', id=sale.id)  
            
    else:
        form = Adding_sales()

    
    if product.quantity <= 5 and not message:
        message = "Attention, le stock est faible !"
    
    context = {
        'message': message,
        'product': product,
        'form': form,
    }

    return render(request, 'sale.html', context)  
        


#  facturation et sauvegarde

@login_required(login_url='login')
def billing(request, id):
    sale = get_object_or_404(Sale, id=id)
    customer = sale.customer
    quantity = sale.quantity
    sale_date = sale.sale_date
    total_amount = sale.total_amount
    product = sale.product

    bill = Bill(customer=customer, quantity=quantity, sale_date=sale_date, total_amount=total_amount, product=product)
    bill.save()

    return redirect('view_bill', id=sale.id)



# affichage de la facture

@login_required(login_url='login')
def view_bill(request,id):
    sale = get_object_or_404(Sale, id=id)
    customer = sale.customer
    quantity = sale.quantity
    sale_date = sale.sale_date
    total_amount = sale.total_amount
    product = sale.product

    context = {
        'customer': customer,
        'quantity': quantity,
        'sale_date': sale_date,
        'total_amount': total_amount,
        'product': product.name,
        'id': sale.id,
        'unit_price': product.price,
    }

    return render(request, 'viewBill.html',context)





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