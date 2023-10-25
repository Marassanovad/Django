from django.contrib import admin
from .models import User, Product, Order

# Register your models here.
@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)

@admin.action(description="Добавить 100 ед. продукта")
def update_quantity(modeladmin, request, queryset):
    queryset.update(count=100)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    fields = ['name', 'email', 'phone_number', 'address',
              'date']
    readonly_fields = ['date']
    ordering = ['name', '-phone_number']
    search_fields = ['email']
    search_help_text = 'Поиск по Email'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    fields = ['name', 'description', 'price', 'count',
              'date']
    readonly_fields = ['date']
    ordering = ['name', '-count']
    search_fields = ['name']
    search_help_text = 'Поиск по Name'
    actions = [reset_quantity, update_quantity]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']
    fields = ['customer', 'products', 'total_price', 'date_ordered']
    readonly_fields = ['date_ordered']
    ordering = ['-total_price', 'date_ordered']
    list_filter = ['date_ordered']
    search_fields = ['customer']
    search_help_text = 'Поиск по Client'

# admin.site.register(User, UserAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Order, OrderAdmin)
