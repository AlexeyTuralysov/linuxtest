from django.urls import path
from .views import ProductView ,ProductRetrieveUpdateDestroyView
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('products/', ProductView.as_view(), name='task-list-create'),
    #path('products/<int:pk>/', ProductView.as_view(), name='product-retrieve-update-destroy'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]