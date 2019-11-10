from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.permissions import (IsAuthenticated, IsAdminUser, AllowAny)

from .models import Product
from .renderers import ProductJSONRenderer
from .serializers import ProductSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = (ProductJSONRenderer,)
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return Product.objects
