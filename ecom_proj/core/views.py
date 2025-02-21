from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import UserSerializer,ProductSerializer,CartItemSerializer,CartSerializer
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Product, Cart,CartItem
from rest_framework import status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema



#paystack.api_key = settings.STRIPE_SECRET_KEY

@extend_schema(responses={200: UserSerializer},
               methods = ['POST'],
               request= UserSerializer,
)              
@api_view(['POST'])
@permission_classes([AllowAny])
def CreateUserView(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    
@extend_schema(responses={200: ProductSerializer(many=True)},
               methods = ['GET'])
@extend_schema(responses= {201: ProductSerializer},
               methods =['POST'],
               request= ProductSerializer)

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
    

@extend_schema(responses= ProductSerializer )
@api_view(['GET'])
@permission_classes([AllowAny])
def ProductDetailview(request, pk):
    queryset = get_object_or_404(Product, pk=pk)
    serializer=ProductSerializer(queryset)
    return Response(serializer.data, status=status.HTTP_200_OK)

@extend_schema(responses= CartSerializer,
                methods=["GET"]
                )
@extend_schema(responses= CartSerializer,
                methods=["POST"],
                request= CartSerializer)
@api_view(['GET','POST'])
@permission_classes([AllowAny])
def CartView(request):
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
    
@extend_schema(responses= CartSerializer,
                methods=["GET"])
@extend_schema(responses= CartSerializer,
                methods=["PUT"],
                request=CartSerializer)
@extend_schema(responses= CartSerializer,
                methods=["DELETE"])

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def CartDetailView(request, pk):
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

@extend_schema(
    methods=["DELETE"],
    responses={
         204: {"description": "Item removed from cart"},
        404: {"description": "Item not found"},
    }
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def delete_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    cart_item.delete()
    return Response({"message": "Item removed from cart"}, status=status.HTTP_204_NO_CONTENT)







    




