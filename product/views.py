from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from product.models import Product
from product.serializers import ProductSerializer


class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrivAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer