from django.contrib import admin

# Register your models here.
from .models import Task,Products

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Перечислите поля, которые вы хотите видеть в списке объектов
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

admin.site.register(Task, TaskAdmin)
admin.site.register(Products, ProductsAdmin)
