from django.urls import path
from . import views
from .views import home, contacts

# app_name = "product"

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('basket/', views.basket, name='basket'),
    path('login/', views.login, name='login'),
    path('product1/', views.product1, name='product1'),
    path('card/', views.card, name='card'),
    path('checkout', views.checkout, name='checkout'),
]
