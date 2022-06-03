from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), 
    
    # USER ACCOUNT
    path('loginUser', views.loginUser,name='loginUser'),
    path('registerUser', views.registerUser,name='registerUser'),
    path('account', views.userAccount, name='userAccount'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    
    # SITE PAGES
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('wishlist/',views.wishlist, name='wishlist'),
    path('shop/',views.shop, name='shop'),
    path('shop_col/',views.shop_col_4, name="shop_col_4"),
    path('blog/',views.blog, name='blog'),
    path('blog_details/<int:pk>',views.blog_details, name='blog_details'),
    path('compare/',views.compare, name='compare'),
    path('payment/<str:ref>/',views.payment,name='payment'),
    path('initiate/', views.initiate_payment,name='initiate_payment'),
    path('trial_payment/<str:ref>/',views.verify_payment,name='verify_payment'),
    path('thank_you/',views.thank_you,name='thank_you'),
    path('faq/',views.faq,name='faq'),
    path('item_detail/<int:item_id>',views.item_detail, name='item_detail'),
    
    # URL for Cart and Checkout
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/checkout/',views.checkout, name='checkout'),

    # URL for Compare
    path('compare_item/<int:cart_id>/', views.compare_item, name="compare_item"),
    path('remove_comp_item/<int:cart_id>/', views.remove_comp_item, name="remove_comp_item"),

    # URL for Wishlist 
    path('add_to_wishlist/<int:cart_id>/', views.add_to_wishlist, name="add_to_wishlist"),
    path('remove_wishlist_item/<int:cart_id>/', views.remove_wishlist_item, name="remove_wishlist_item"),
    path('add/<int:item_id>/', views.add,name='add'),
    
    

    

    
]