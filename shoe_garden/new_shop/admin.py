from django.contrib import admin
from .models  import *

class FrontPageCarouselAdmin(admin.ModelAdmin):
    list_display = ('offer_title', 'offer_product', 'discount',)
    list_filter = ('offer_title',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title", )}

class ItemSecondaryImageAdmin(admin.TabularInline):
    model = ItemSecondaryImage
class ItemsAdmin(admin.ModelAdmin):
        list_display = ('name', 'brand', 'sizes_available', 'display_in', 'price', 'item_status')
        list_filter = ('name', 'category', 'brand', 'display_in','item_status',)
        inlines = [ItemSecondaryImageAdmin,]

class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularInline]
        
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at',)
    list_filter = ('user','product','created_at',)
    # search_fields = ('product',)

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at',)
    list_filter = ('user','product','created_at',)

admin.site.register(FrontPageCarousel, FrontPageCarouselAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CardProduct)
admin.site.register(Feedback)
admin.site.register(OurTeam)
admin.site.register(BlogPost)
admin.site.register(Item, ItemsAdmin)
admin.site.register(Offer)
admin.site.register(Filter_price)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Compare)
admin.site.register(Wishlist, WishlistAdmin)

admin.site.register(Brand)

admin.site.register(ContactInfo)
admin.site.register(Payment)