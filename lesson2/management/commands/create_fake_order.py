import random
from django.core.management.base import BaseCommand
from lesson2.models import User, Product, Order

class Command(BaseCommand):
    help = "Generate fake data."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            for k in range(1, 2):
                user = User.objects.filter(pk=k).first()
                order = Order(customer=user, total_price=random.randint(1000, 100000))
                order.save()
                for j in range(1, random.randint(1, 4)):
                    order.products.add(Product.objects.filter(pk=random.randint(1, 15)).first())
