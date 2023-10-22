from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
import logging
import datetime
from .models import User, Product, Order
from django.utils import timezone
from .forms import UserForm, ProductForm

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="./logs/lesson2.log", filemode='a', format='%(levelname)s %(message)s')

def index(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.datetime.now()))
    return HttpResponse("Hello, world!")

def get_all_user(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.datetime.now()))
    users = User.objects.all()
    return render(request, "user.html", {'users': users})

def get_all_product(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.datetime.now()))
    products = Product.objects.all()
    return render(request, "product.html", {'products': products})
#
def get_all_order(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.datetime.now()))
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

def user_registration(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.datetime.now()))
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f'Получили {name=}, {email=}, {phone_number=}, {address=}, {image.name=}.')
            user = User(name=name, email=email, phone_number=phone_number, address=address, image=image.name)
            user.save()
            message = 'Пользователь сохранён'
        return render(request, 'user_reg.html', {'form': form, 'message': message})
    else:
        form = UserForm()
        message = 'Заполните форму'
        return render(request, 'user_reg.html', {'form': form, 'message': message})

# def choice_product(request):
#     if request.method == 'POST':
#         form = ChoiseProductForm(request.POST)
#         if form.is_valid():
#             product_id = form.cleaned_data['id']
#             choice = form.cleaned_data['choice']
#             logger.info(f'Получили {product_id=}, {choice=}.')
#         return edit_product(request, pk=product_id,choice=choice)
#     else:
#         form = ChoiseProductForm()
#         message = 'Заполните форму'
#         return render(request, 'choice_edit_product.html', {'form': form, 'message': message})
def edit_product(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.datetime.now()))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            product_id = form.cleaned_data['id']
            datas = {"name": form.cleaned_data['name'], "description": form.cleaned_data['description'], "price": form.cleaned_data['price'], "count": form.cleaned_data['count'], "image": form.cleaned_data['image']}
            #
            logger.info(f'Получили {datas["name"]=}, {datas["description"]=}, {datas["price"]=}, {datas["count"]=}.')
            product = get_object_or_404(Product, pk=product_id)
            for data in datas:
                if datas[data] != "" and data == "name":
                    product.name = datas[data]
                elif datas[data] != "" and data == "description":
                    product.description = datas[data]
                elif datas[data] != "" and data == "price":
                    product.price = datas[data]
                elif datas[data] != "" and data == "count":
                    product.count = datas[data]
                elif datas[data] != "" and data == "image":
                    image = datas[data]
                    fs = FileSystemStorage()
                    fs.save(image.name, image)
                    product.image = image.name
                product.save()
            message = 'Продукт обновлен'
        return render(request, 'edit_product.html', {'form': form, 'message': message})
    else:
        form = ProductForm()
        message = 'Заполните форму'
        return render(request, 'edit_product.html', {'form': form, 'message': message})