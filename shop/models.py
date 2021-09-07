from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categorie(models.Model):
    category=models.CharField(default='', max_length=30)
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.category


class Product(models.Model):
    product_id=models.AutoField
    category=models.CharField(default='', max_length=30)
    sub_category=models.CharField(default='', max_length=30)
    product_name=models.CharField(default='', max_length=60)
    desc=models.CharField(default='', max_length=300)
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images", default='')


    def __str__(self):
        return self.product_name


class address(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(default='', max_length=30)
    email=models.CharField(default='', max_length=30)
    phone=models.CharField(default='', max_length=12)
    add=models.CharField(default='', max_length=50)
    city=models.CharField(default='', max_length=30)
    state=models.CharField(default='', max_length=30)
    pin=models.IntegerField(default=0)

    def __str__(self):
        return self.name


class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    orderjson=models.CharField(default='', max_length=1000)
    address=models.OneToOneField(address, models.CASCADE)

    def __str__(self):
        return self.order_id




class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    cartjson=models.CharField(default='', max_length=1000)
    address=models.OneToOneField(address, models.CASCADE)