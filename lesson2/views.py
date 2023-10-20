from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
import logging
import datetime
from .models import User, Product, Order
from django.utils import timezone

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="./logs/lesson2.log", filemode='a', format='%(levelname)s %(message)s')

def index(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    return HttpResponse("Hello, world!")

def get_all_user(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    users = User.objects.all()
    return render(request, "user.html", {'users': users})

def get_all_product(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    products = Product.objects.all()
    return render(request, "product.html", {'products': products})
#
def get_all_order(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    orders = Order.objects.all()
    return render(request, "order.html", {'orders': orders})

def user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user).order_by('-id')
    return render(request, 'user_orders.html', {'user': user, 'orders': orders})

def user_fillter_products(request, user_id, date):
    user = get_object_or_404(User, pk=user_id)
    start = timezone.now() - datetime.timedelta(days=date)
    # start = datetime.date.today() - datetime.timedelta(days=date)
    orders = Order.objects.filter(customer=user, date_ordered__gte=start).order_by('-date_ordered')
    return render(request, 'user_products_order.html', {'user': user, 'orders': orders})