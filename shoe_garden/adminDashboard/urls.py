from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_login', views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/statistics', views.statistics, name='statistics'),
    path('dashboard/reports', views.reports, name='reports'),
    # path('invoice', views.invoice, name='invoice'),
    path('profile', views.profile, name='profile'),

    
    path('vendor/list', views.vendor_list, name='vendor_list'),
    path('vendor/add', views.create_vendor, name='create_vendor'),
    
    path('user/list', views.user_list, name='user_list'),
    path('user/add', views.create_user, name='create_user'),
    
    path('coupon/list', views.coupon_list, name='coupon_list'),
    path('coupon/add', views.create_coupon, name='create_coupon'),
    
    path('product/categories', views.categories, name='categories'),
    path('category/sub', views.category_sub, name='category_sub'),
    
    path('product/add', views.product_add, name='product_add'), # get and post req. to add product
    path('<int:id>/', views.product_add, name='update_product'), # get and post req. to update
    path('product/list', views.product_list, name='product_list'),   # get request to retrieve and display all products
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    
    path('<int:id>/', views.update_order, name='update_order'),
    path('order/', views.orders, name='orders'),

     path('payments/', views.payments, name='payments'),
    
    
    
]