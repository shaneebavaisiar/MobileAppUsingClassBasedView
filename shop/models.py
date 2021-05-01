from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Brands(models.Model):
    brand_name=models.CharField(max_length=120,unique=True)
    def __str__(self):
        return self.brand_name
class Mobile(models.Model):
    mobile_name=models.CharField(max_length=120)
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE)
    price=models.IntegerField(null=False)
    model_name=models.CharField(max_length=80)
    specs=models.CharField(max_length=250)
    description=models.CharField(max_length=120)
    img=models.ImageField(upload_to='images')

    def __str__(self):
        return self.mobile_name

class Order(models.Model):

    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    address=models.CharField(max_length=120)
    user=models.CharField(max_length=120)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    choices=[
        ('ordered','ordered'),
        ('dispatched','dispatched'),
        ('cancelled','cancelled')
    ]
    status=models.CharField(max_length=120,choices=choices,default='ordered')

    def __str__(self):
        return self.user

class Cart(models.Model):
    user=models.CharField(max_length=120)
    # product = models.CharField(max_length=120)
    product = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    # price=models.IntegerField(null=True)






