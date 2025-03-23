from .serializers import ProductSerializer , OrderSerializer , ProductInfoSerializer
from .models import Product , Order , OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.db.models import Max


class productList(generics.ListAPIView):
    queryset = Product.objects.filter(stock__gt=0)
    serializer_class = ProductSerializer


class productDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class orderList(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items").all()
    serializer_class = OrderSerializer


class UserOrderList(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items").all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qr = super().get_queryset()
        return qr.filter(user=user)

class ProductInfo(APIView):
    def get(self , request):
        products = Product.objects.all()
        serial = ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'maxPrice': products.aggregate(maxPrice=Max('price'))['maxPrice']
        })
        return Response(serial.data)

