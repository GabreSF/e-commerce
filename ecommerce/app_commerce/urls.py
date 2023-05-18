from django.urls import path
from app_commerce import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'), 
    path('checkout/', views.checkout, name='checkout'),
]
