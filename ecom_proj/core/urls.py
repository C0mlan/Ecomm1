from django.urls import path
from . import views
# from .views import ProductListCreateView

urlpatterns = [
    path('home/<str:pk>/', views.ProductDetailview, name='products'),
    path('products/', views.ProductListCreateView, name='products-list-create'),

    path('cart/', views.cartview, name='cart-list-create'),
    path('cart/<str:pk>', views.cartdetailview, name='cart-detail'),

    

    



]
