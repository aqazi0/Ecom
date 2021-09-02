from django.contrib import admin

# Register your models here.


from .models import Product, categorie

admin.site.register(Product)
admin.site.register(categorie)
