from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='aboutus'),
    path('contact/', views.contact, name='contactus'),
    path('tracker/', views.track, name='trackstatus'),
    path('search/', views.search, name='search'),
    path('prodview<int:myid>', views.prodview, name='product'),
    path('category<int:catid>', views.catview, name='category'),
    path('checkout', views.checkout, name='chout'),
    path('cart', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('hanlogin/', views.hanlogin, name='hanlogin'),
]