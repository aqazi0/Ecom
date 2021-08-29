from django.db import models

# Create your models here.



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




# class signup(models.Model):
#     userid=models.AutoField(primary_key=True)
#     username=models.CharField(max_length=15, default='',unique=True)
#     email=models.CharField(max_length=30, default='', unique=True)
#     pass1=models.CharField(max_length=20,default='')
#     pass2=models.CharField(max_length=20,default='')

#     def __str__(self):
#         return self.username