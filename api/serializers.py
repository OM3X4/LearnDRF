from rest_framework import serializers
from .models import Product , User , Order , OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id' , 'name' , 'stock' ,  'price')

    def validate_price(self , value):
        if value <= 0:
            raise serializers.ValidationError("Price Must Be Greater Than Zero")


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product" , "order" , "quantity")


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True , read_only=True)

    class Meta:
        model = Order
        fields = ("user" , 'id' , 'createdAt' , 'status' , 'items')

class ProductInfoSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    products = ProductSerializer(many=True)
    maxPrice = serializers.DecimalField(max_digits=8 , decimal_places=2)