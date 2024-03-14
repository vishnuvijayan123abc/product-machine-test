from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    options= (("available","available"),
              ("sold","sold")
        
       )
    status = models.CharField(max_length=50,choices=options,default="available")


    def __str__(self):
        return self.name



class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    oder_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

