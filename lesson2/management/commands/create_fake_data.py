import random
from django.core.management.base import BaseCommand
from lesson2.models import User, Product


class Command(BaseCommand):
    help = "Generate fake data."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'mail{i}@mail.ru', phone_number=random.randint(1000000000, 9999999999), address=f'street{i}, house{random.randint(0,30)}')
            user.save()
        for i in range(1, count + 1):
            product = Product(name=f'Name{i}', description=f'NEW PRODUCT', price=random.randint(100, 1000), count=random.randint(100, 1000))
            product.save()


