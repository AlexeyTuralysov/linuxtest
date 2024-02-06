from django.urls import path
from .views import TaskListCreateView,Products

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('products/', Products.as_view(), name='products'),
]