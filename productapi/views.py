from django.shortcuts import render
from productapi.serializers import UserSerializer,ProductSerializer,OderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from productapi.models import Product,Order
from rest_framework import serializers
from rest_framework import authentication,permissions
from rest_framework import generics
from django.db.models import Count
# Create your views here.


class UserSignUpView(APIView):
    def post(self,request,*args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.error)

class ProductView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]
    serializer_class=ProductSerializer
    queryset=Product.objects.all() 

class UserProductView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProductSerializer
    queryset=Product.objects.all()


    def create(self, request, *args, **kwargs):
        raise serializers.validationError("permission denied")
    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    def update(self, request, *args, **kwargs):
       raise serializers.ValidationError("permission denied")
    
class OderView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=OderSerializer

    def get_queryset(self):
       product_id=self.kwargs.get("product_id")
       return Order.objects.filter(product=product_id)
    
    def perform_create(self, serializer):
        product_id=self.kwargs.get("product_id")
        serializer.save(user=self.request.user,product_id=product_id)
class oderReadView(viewsets.ModelViewSet):
     authentication_classes=[authentication.TokenAuthentication]
     permission_classes=[permissions.IsAuthenticated]

     serializer_class=OderSerializer
     def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    

class ProductCountView(APIView):

    def get(self, request):
        products = Product.objects.annotate(total_orders=Count('order')).order_by('-total_orders')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)



