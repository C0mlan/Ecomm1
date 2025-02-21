from django.urls import path
from . import views


urlpatterns = [
    path('products/<str:pk>/', views.ProductDetailview, name='products'),
    path('products/', views.ProductListCreateView, name='products-list-create'),

    path('cart/', views.CartView, name='cart-list-create'),
    path('cart/<str:pk>', views.CartDetailView, name='cart-detail'),
    path('cart-item/<int:pk>/', views.delete_cart_item, name='cart-item-delete'),

    

    



]
