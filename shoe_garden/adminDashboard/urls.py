from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_login', views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/transactions', views.transactions, name='transactions'),
    path('dashboard/reports', views.reports, name='reports'),
    path('invoice', views.invoice, name='invoice'),
    path('profile', views.profile, name='profile'),

    
    path('vendor/list', views.vendor_list, name='vendor_list'),
    path('vendor/add', views.create_vendor, name='create_vendor'),
    
    path('user/list', views.user_list, name='user_list'),
    path('user/add', views.create_user, name='create_user'),
    
    path('coupon/list', views.coupon_list, name='coupon_list'),
    path('coupon/add', views.create_coupon, name='create_coupon'),
    
    path('category/main', views.category_main, name='category_main'),
    path('category/sub', views.category_sub, name='category_sub'),
    
    path('product/add', views.product_add, name='product_add'),
    path('product/list', views.product_list, name='product_list'),
    
    
    path('order/history', views.orders, name='orders'),
    
    
    
]