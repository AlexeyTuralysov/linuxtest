# myapp/views.py
from rest_framework import generics, viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all() #получение инфы от бд
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
