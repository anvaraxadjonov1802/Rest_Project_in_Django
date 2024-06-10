from .serializers import ProductSerializers
from rest_framework import viewsets, permissions
from .models import Product

class ProductViwset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializers