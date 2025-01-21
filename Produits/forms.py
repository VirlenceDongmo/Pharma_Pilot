from django.forms import ModelForm
from .models import Product
from django import forms

class Add_product(ModelForm) :

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity', 'description', 'expiration_date', 'image']

        widgets={
            'name':forms.TextInput(
                attrs={
                    'placeholder':"Enter the product name",
                    'class':"form-control",
                }
            ),

            'category':forms.Select(
                attrs={
                    'class':"form-control",
                }
            ),

            'price':forms.NumberInput(
                attrs={
                    'placeholder':"Enter the product price",
                    'class':"form-control",
                }
            ),

            'quantity':forms.NumberInput(
                attrs={
                    'placeholder':"Enter the product quantity",
                    'class':"form-control",
                }
            ),

            'description':forms.Textarea(
                attrs={
                    'placeholder':"Enter the product description",
                    'class':"form-control",
                    'rows':"2",
                }
            ),

            'expiration_date':forms.DateInput(
                attrs={
                    'class':"form-control",
                    'type':"date",
                }
            ),

            'image':forms.FileInput(
                attrs={
                    'class':"form-control-file",
                }
            ),
        }

        def __init__(self, *args, **kwargs):
            super(Add_product,self).__init__(self, *args, **kwargs)
            
            self.fields['name'].error_messages={
                'required':"The product name is mandatory",
                'invalid':"Please fill in the name space with a valid value",
            }

            self.fields['category'].error_messages={
                'required':"The product category is mandatory",
                'invalid':"Please select a category valid for your product",
            }

            self.fields['price'].error_messages={
                'required':"The product price is mandatory",
                'invalid':"Please fill in the price space with a valid value",
            }

            self.fields['quantity'].error_messages={
                'required':"The product quantity is mandatory",
                'invalid':"Please fill in the quantity space with a valid value",
            }

            self.fields['description'].error_messages={
                'required':"The product description is mandatory",
                'invalid':"Please fill in the description space with a valid value",
            }

            self.fields['expiration_date'].error_messages={
                'required':"The product expiration_date is mandatory",
                'invalid':"Please fill in the expiration date space with a valid value",
            }
