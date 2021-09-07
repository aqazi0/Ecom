from django.contrib import admin

# Register your models here.


from .models import Product, UserProfile, address, categorie, order

admin.site.register(Product)
admin.site.register(categorie)
admin.site.register(order)
admin.site.register(address)
admin.site.register(UserProfile)
