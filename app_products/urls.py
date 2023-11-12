from django.contrib import admin
from django.urls import path ,re_path
from . import views
from django.contrib.auth.decorators import login_required
from .views import delete_all

urlpatterns = [
    path('',views.products, name='products'),
    path('delete_all/', delete_all, name='delete_all'),
    path('detail/<slug:slug>/',views.detail, name='detail'),
    re_path(r'add/$', login_required(views.product_add,login_url="/login"), name='product_add'),
    re_path(r'cart/add/(?P<slug>[\w-]+)/$', views.cart_add, name='cart_add'), 
    re_path(r'cart/delete/(?P<slug>[\w-]+)/$', views.cart_delete, name='cart_delete'),
    re_path(r'cart/reduce/(?P<slug>[\w-]+)/$', views.cart_reduce, name='cart_reduce'),
    re_path(r'cart/list/$', views.cart_list, name='cart_list'),
] 