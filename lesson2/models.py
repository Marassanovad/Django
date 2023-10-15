from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.TextField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, date:{self.date}'

class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    # image = models.ImageField(upload_to='products/')

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)


def py():
    return None