from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",views.register, name="index"),
    path("login/",views.login, name="login"),
    path("home/",views.home, name="home"),
    path("home/<str:name>",views.homeview, name="homeview"),
    path("shop/",views.shop, name="shop"),
    path("shop/<str:name>",views.shopview, name="shopview"),
    path("shop2/",views.shop2, name="shop2"),
    path("cart/",views.cart, name="cart"),
    path("customize/",views.customize, name="customize"),
    path("order/",views.order, name="order"),
    path("feedback/",views.feedback, name="feedback")
]