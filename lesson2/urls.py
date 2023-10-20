from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.get_all_user, name='all_user'),
    path('product/', views.get_all_product, name='all_product'),
    path('order/', views.get_all_order, name='all_order'),
    path('user/<int:user_id>/', views.user_orders, name='user_orders'),
    path('user/<int:user_id>/<int:date>', views.user_fillter_products, name='user_fillter_products'),
    # path('post/<int:post_id>/', post_full, name='post_full'),
    # path('about/', views.about, name='about'),
]