from django.db import models

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