from django.urls import path
from . import views


app_name = 'store'


urlpatterns = [
    path("", views.homes, name="home"),
    #path('order', views.order, name='product_details'),
    #path("<int:id>", views.order, name='product_details'),
    #path("cart", views.cart, name="cart_page"),
    path("orders", views.orders, name='addProd')
]
