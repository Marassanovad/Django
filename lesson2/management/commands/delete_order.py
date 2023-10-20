from django.core.management.base import BaseCommand


from lesson2.models import Order


class Command(BaseCommand):
    help = "Delete product by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            order.delete()
        self.stdout.write(f'{order}')