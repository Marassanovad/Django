from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import logging
from datetime import datetime


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="./logs/lesson1.log", filemode='a', format='%(levelname)s %(message)s')

def index(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    return HttpResponse("Hello, world!")


def main(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    return render(request, "main.html")

def about(request):
    logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    return render(request, "about.html")
