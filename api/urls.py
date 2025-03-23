from django.urls import path
from . import views


urlpatterns = [
    path('products/' , views.productList.as_view()),
    path('products/<int:pk>/' , views.productDetails.as_view()),
    path("orders/" , views.orderList.as_view()),
    path("userorders/" , views.UserOrderList.as_view() , name='user-orders'),
    path('products/info/' , views.ProductInfo.as_view())
]
