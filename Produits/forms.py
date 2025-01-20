from django.forms import ModelForm
from .models import Product

class Add_product(ModelForm) :

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity', 'description', 'expiration_date', 'image']