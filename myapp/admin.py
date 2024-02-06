from django.contrib import admin

# Register your models here.
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Перечислите поля, которые вы хотите видеть в списке объектов

admin.site.register(Task, TaskAdmin)