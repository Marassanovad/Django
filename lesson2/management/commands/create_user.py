from django.core.management.base import BaseCommand
from lesson2.models import User


class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='Djeck', email='smit@example.com',phone_number='secret', address='secret')
        user.save()
        self.stdout.write(f'{user}')

