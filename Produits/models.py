from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model) :
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to='media/')


    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta :
        ordering = ['-add_date']


    def quantity_status(self) :
        if self.quantity == 0 :
            return 'red'
        elif self.quantity < 10 or self.quantity == 10 :
            return 'orange'
        else :
            return 'green'



class Customer(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Sale(models.Model) :
    sale_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.CharField(max_length=100)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer


class Bill(models.Model) :
    quantity = models.PositiveIntegerField(default=0)
    sale_date = models.DateTimeField(auto_now_add=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.CharField(max_length=100)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Le reçu de {self.customer.name}"

    
