from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Task, Products
from .serializers import TaskSerializer,ProductsSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class Products(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer