from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartList.as_view(), name='cart-list'),
    path('cart/add/', views.AddToCart.as_view(), name='add-to-cart'),
    path('cart/delete/<int:pk>/', views.DeleteCart.as_view(), name='delete-cart'),
]