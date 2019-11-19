from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Product
from .renderers import ProductJSONRenderer
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = (ProductJSONRenderer,)
    permission_classes = [
        AllowAny,
    ]

    def get_queryset(self):
        return Product.objects.all().order_by("-id")
