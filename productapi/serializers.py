from productapi.models import Product,Order
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=["id","name","description","size","color","status"]
        read_only_fields=["id","status"]
class OderSerializer(serializers.ModelSerializer):
    product=serializers.StringRelatedField()
    user=serializers.StringRelatedField()
    class Meta:
        model=Order
        fields=["id","product","quantity","oder_date","user"] 
        read_only_fields=["id","oder_date","product","user"]       

