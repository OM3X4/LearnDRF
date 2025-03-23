from django.shortcuts import render , get_object_or_404
from django.http import JsonResponse
from .serializers import ProductSerializer , OrderSerializer
from .models import Product , Order , OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serial = ProductSerializer(products , many=True)
    return Response(serial.data , status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request , pk):
    product = get_object_or_404(Product , pk=pk)
    serial = ProductSerializer(product)
    return Response(serial.data , status=status.HTTP_200_OK)


@api_view(["GET"])
def order_list(request):
    orders = Order.objects.prefetch_related("items").all()
    serial = OrderSerializer(orders , many=True)
    return Response(serial.data , status=status.HTTP_200_OK)