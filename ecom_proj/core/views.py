from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import UserSerializer,ProductSerializer,CartItemSerializer,CartSerializer
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Product, Cart,CartItem
from rest_framework import status, generics
from rest_framework.response import Response



#paystack.api_key = settings.STRIPE_SECRET_KEY
@api_view(['POST'])
@permission_classes([AllowAny])
def CreateUserView(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def ProductListCreateView(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def ProductDetailview(request, pk):
    queryset = get_object_or_404(Product, pk=pk)
    serializer=ProductSerializer(queryset)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def cartview(request):
    if request.method == 'GET':
        carts= Cart.objects.all()
        serializer=CartSerializer(carts,many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method =='POST':
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
@api_view(['Get', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])

def cartdetailview(request, pk):
    cart = get_object_or_404(Cart, pk=pk)

    if request.method == 'GET':
        serializer= CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer =CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        cart.delete()
        return Response({'message':'Cart deleted sucessfully'}, status= status.HTTP_204_NO_CONTENT)






    




