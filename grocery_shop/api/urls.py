from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/products', views.products_api,name='products-api'),
    path('api/categories', views.categories_api,name='categories-api'),
]