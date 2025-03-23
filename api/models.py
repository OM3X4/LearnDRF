from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True , default='' , blank=True)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/' , blank=True , null=True)

    @property
    def inStock(self):
        return self.stock > 0

    def __str__(self):
        return self.name


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending"
        CANCELLED = "Cancelled"
        CONFIRMED = "Confirmed"

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10 , choices=Status , default=Status.PENDING)

    products = models.ManyToManyField(Product , through="OrderItem" , related_name='orders')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='items')
    product = models.ForeignKey(Product , on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    @property
    def total(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} * {self.product} in Order {self.order.id}"




