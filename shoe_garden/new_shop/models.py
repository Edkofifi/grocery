from distutils.command.upload import upload
import secrets
from .paystack import Paystack
from django.db import models
from django.contrib.auth.models import User
class FrontPageCarousel(models.Model):
    background_image = models.ImageField(upload_to = 'site_images/carousel_img')
    discount = models.IntegerField()
    offer_title = models.CharField(max_length = 100)
    offer_product = models.CharField(max_length = 100, null=True)
    
    def __str__(self):
        return self.offer_title
    
class Offer(models.Model):
    img = models.ImageField(upload_to = 'site_images/offer_img')
    discount = models.IntegerField()
    product_type = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.product_type
   
class Brand(models.Model):
    name = models.CharField(verbose_name="Brand Name", max_length=30,blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Brands'        

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Category Title")
    slug = models.SlugField(max_length=55, verbose_name="Category Slug")
    description = models.TextField(blank=True, verbose_name="Category Description")
    # category_image = models.ImageField(upload_to='site_images', blank=True, null=True, verbose_name="Category Image")
    is_active = models.BooleanField(verbose_name="Is Active?")
    is_featured = models.BooleanField(verbose_name="Is Featured?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title
    
    # def save(self, **kwargs):
    #     slug = '%s' % (self.title)
    #     unique_slugify(self, slug)
    #     super(Category, self).save()
    
class Filter_price(models.Model):
    price_range_choice =[
        ('0 TO 10', '0 TO 10'),
        ('11 TO 20', '11 TO 20'),
        ('21 TO 50', '21 TO 50'),
        ('51 TO 100', '51 TO 100'),
        ('101 TO Above', '101 TO Above'),
        
    ]
    price_range = models.CharField(choices =price_range_choice, max_length= 25)


class Item(models.Model):
    # Gender choice
    M ='Male'
    F='Female'
    U='Unisex'
    
    gender_choice = [
        (M,'Male'),
        (F,'Female'),
        (U,'Unisex')
    ]
    
    # Product Size    
    product_size_choice = [
    ("X", 'X'),
    ("M", 'M'),
    ("L" ,'L'),
    ("XL", 'XL'),
    ("XLL", 'XXL'),
    ]

    item_dispay_choices =[
        ("Featured", 'Featured'),
        ("Best Seller", "Best Seller"),
        ("Shop", "Shop")
    ]
    stock_status = [
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock'),
      
    ]

    name = models.CharField(max_length=100, verbose_name='Item Name')    
    image = models.ImageField(upload_to = 'site_images',verbose_name='Item Image')    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='item_category')
    description = models.TextField(verbose_name='Item Description')    
    display_in = models.CharField(choices=item_dispay_choices, max_length=50, null= True, verbose_name='Diplayed In')
    item_status = models.CharField(choices=stock_status, max_length=50, null= True, verbose_name='Item Status')
    has_discount = models.BooleanField(default = False, verbose_name='Has Discount')
    discount = models.IntegerField(blank=True, null=True, verbose_name='Discount')
    price = models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=5)
    price_filter_range = models.ForeignKey(Filter_price, on_delete = models.SET_NULL, null= True)
    discount_price = models.FloatField(blank=True, null=True, verbose_name='Discount Price')
    quantity_available = models.IntegerField(verbose_name='Quantity in Stock')
    

    # brand = models.CharField(max_length=50, verbose_name='Item Brand')
    # brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null = True)
    # gender = models.CharField(choices=gender_choice, max_length=10, verbose_name='Gender')
    # sizes_available = models.CharField(choices=product_size_choice, max_length=50, verbose_name='Size Avaailable')


    def __str__(self):
        return self.name
    
    @property
    def item_status_color(self):
        if self.item_status == 'In Stock':
            item_color = 'primary'
        elif self.item_status =='Not Available':
            item_color = 'danger'
        elif self.item_color == 'Ready to Ship':
            item_color = 'success'
        elif self.item_status == 'Sold Out':
            item_color = 'secondary'
        elif self.item_status == 'Temporarily Out-of-Stock':
            item_color = 'info'
        return item_color

class ItemSecondaryImage(models.Model):
    product = models.ForeignKey(Item, verbose_name="Item", on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'site_images/other_item_img',verbose_name='Secondary Image')
    
    def __str__(self):
        return self.product.name


class Order(models.Model):
    order_status=[
        ('Created','Created'),
        ('Processing','Processing'),
        ('Cancelled','Cancelled'),
        ('Shipped','Shipped'),
        ('Completed','Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100,null = True,)
    last_name = models.CharField(max_length = 100,null = True, blank=True)
    country = models.CharField(max_length = 100,null = True,)
    region = models.CharField(max_length = 100,null = True,)
    town = models.CharField(max_length = 100,null = True,)
    address1 = models.CharField(max_length = 100,null = True,)
    address2 = models.CharField(max_length = 100,null = True,)
    GPS = models.CharField(max_length = 100, null = True,)
    phone = models.CharField(max_length = 100,null = True,)
    email = models.EmailField(max_length = 100,null = True,)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    order_note = models.CharField(max_length = 100, null = True,blank=True)
    ref = models.CharField(max_length =200, null = True,blank=True)
    verified = models.BooleanField(default = False)
    status = models.CharField(max_length =200, choices=order_status,default="Pending")
    date = models.DateField(auto_now_add= True,)
    
    class Meta:
        ordering = ('-date',)
    
    def __str__(self) -> str:
        return f'Payment: {self.amount}'
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Order.objects.filter(ref = ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
        
    def amount_value(self) -> int:
        return self.amount *100
                
    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
                self.status = "Processing"
            self.save()
        if self.verified:
            return True
        return False
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null = True,)
    product_name = models.CharField(max_length = 100,null = True,)
    product_image = models.ImageField(upload_to = 'site_images/OrderItem',null = True,)
    quantity = models.CharField(max_length = 100,null = True,)
    price = models.CharField(max_length = 100,null = True,)
    total = models.CharField(max_length = 100,null = True,)

    
    def __str__(self):
        return self.order.user.username

class CardProduct(models.Model):
    img = models.ImageField(upload_to = 'site_images/card_img')
    start_price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category
    
class Feedback(models.Model):
    username= models.CharField(max_length=100)
    feedback_content = models.TextField()
    profile_pic = models.ImageField(upload_to ='site_images/feedback_img')
    
    def __str__(self):
        return self.username
    
class OurTeam(models.Model):
    member_name = models.CharField(max_length = 100)
    member_position = models.CharField(max_length= 100)
    member_pic = models.ImageField(upload_to = 'site_images/team_img')
    
    def __str__(self):
        return self.member_name

class BlogPost(models.Model):
    author = models.CharField(max_length=100)
    published_date = models.DateField(auto_now=True)
    blog_title = models.CharField(max_length = 100)
    blog_image = models.ImageField(upload_to = 'site_images/blog_img')
    blog_desc = models.TextField(null = True)
    
    def __str__(self):
        return self.author
    

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Item, verbose_name="Item", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.user)
    
    
    
class Compare(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Item, verbose_name="Item", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Wishlist(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Item, verbose_name="Item", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self):
        return str(self.user)
    
    
    
class ContactInfo(models.Model):
    address = models.CharField(verbose_name='Address Info', max_length=100)
    phone = models.CharField(verbose_name='Phone No', max_length=10)
    email = models.EmailField(max_length = 254, verbose_name= 'Email')
    
    def __str__(self):
        return self.address
        

class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length =200)
    email = models.EmailField()
    verified = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add = True)
    
    
    class Meta:
        ordering = ('-date_created',)
        
    def __str__(self) -> str:
        return f'Payment: {self.amount}'
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref = ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
        
    def amount_value(self) -> int:
        return self.amount *100
                
    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False
        
    