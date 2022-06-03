from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from grocery_shop import settings
from . models import *
from django.core.paginator import Paginator

from . import forms
from django.http import HttpRequest, HttpResponse


from cart.cart import Cart

def homepage(request):
    front_carousels = FrontPageCarousel.objects.all()
    offers = Offer.objects.all()
    featured_items = Item.objects.filter(display_in = "Featured").order_by('-id')[:8]
    # featured_products = FeaturedProduct.objects.all().order_by('-id')[:8]
    best_sellers = Item.objects.filter(display_in = "Best Seller")
    card_products = CardProduct.objects.all()
    feedbacks = Feedback.objects.all().order_by('-id')[:2]
    items = Item.objects.all()
    
    context = {
        'front_carousels' : front_carousels,
        'offers' : offers,
        'items' : items,
        'featured_items' : featured_items,
        'best_sellers' : best_sellers,
        'card_products' : card_products,
        'feedbacks' : feedbacks,
        'items' : items,
    }
    return render(request, 'homepage/index-two.html', context)

def item_detail(request,item_id):
    item = get_object_or_404(Item,pk=item_id)
    item_images = ItemSecondaryImage.objects.filter(product=item)
    context = {
        'item' : item,
        'item_images': item_images
    }
    return render(request,'pages/single-affiliate-product.html',context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('dashboard')
                else:
                    return redirect('homepage')
            else:
                messages.error(request, 'Username or Password is incorrect')
        else:
            messages.error(request, 'All fields must be filled!!')
    return render(request, 'user_account/login.html')

def registerUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['username']

        if password1 == password2:
            #Check username
            if User.objects.filter(username = username).exists():
                messages.error(request, 'This name is already taken')
                return redirect('registerUser')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('registerUser')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name, password=password1, email=email,)
                    user.save()
                    return redirect('loginUser')
        else:
            messages.error(request, 'Passwords do not match')
            # return redirect('register_user')
    return render(request, 'user_account/register.html')

def logoutUser(request):
    logout(request)
    return redirect('homepage')
    
    
def userAccount(request):
    return render(request, 'user_account/account.html')

def about(request):
    feedbacks = Feedback.objects.all().order_by('-id')[:2]
    our_teams = OurTeam.objects.all().order_by('-id')[:4]
    
    context = {
        'feedbacks' : feedbacks,
        'our_teams' : our_teams,
        
    }

    return render(request, 'pages/about-us.html', context)

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_subject = request.POST['message_subject']
        message = request.POST['message']
        send_mail(
            message_subject + ' - Email: ' + message_email,
            message,
            settings.EMAIL_HOST_USER,
            ['atk.eddy@gmail.com']
        )
        
        return render(request, 'pages/contact.html')

    else:
        contacts = ContactInfo.objects.all().order_by('-id')[:1]
        context = {
            'contacts': contacts
        }
        return render(request, 'pages/contact.html',context)

def shop(request):
    categories = Category.objects.all()
    price_filter = Filter_price.objects.all()
    brands = Brand.objects.all()
    CAT_ID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    BRAND_FILTER_ID =   request.GET.get('brands')
    
    if CAT_ID:
        featured_products = Item.objects.filter(category = CAT_ID)
    elif PRICE_FILTER_ID:
        featured_products = Item.objects.filter(price_filter_range = PRICE_FILTER_ID)
    elif BRAND_FILTER_ID:
        featured_products = Item.objects.filter(brand = BRAND_FILTER_ID)
    else:
        featured_products = Item.objects.all()

    page = Paginator(featured_products,12)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
        'categories' : categories,
        'brands' : brands,
        'price_filter' : price_filter
    }

    return render(request, 'pages/shop.html', context)

def shop_col_4(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands
    }
    return render(request, 'pages/shop-four-columns.html', context)


def compare_item(request,cart_id):
    user = request.user
    product = get_object_or_404(Item, id=cart_id)
    item_already_in_cart = Compare.objects.filter(product=cart_id, user=user)
    if item_already_in_cart:
        compare = get_object_or_404(Compare, product=cart_id, user=user)
        compare.save()
    else:
        Compare(user=user, product=product).save()
    return redirect('compare')


    
@login_required(login_url="/loginUser")
def add_to_wishlist(request,cart_id): 
    user = request.user
    product = get_object_or_404(Item, id=cart_id)
    item_already_in_cart = Wishlist.objects.filter(product=cart_id, user=user)
    if item_already_in_cart:
        wishlist = get_object_or_404(Wishlist, product=cart_id, user=user)
        wishlist.save()
        
    else:
        Wishlist(user=user, product=product).save()    
    return redirect('wishlist')

def add(request,item_id):
    user = request.user
    product = get_object_or_404(Item, id=item_id)
    item_already_in_cart = Wishlist.objects.filter(product=item_id, user=user)
    if item_already_in_cart:
        wishlist = get_object_or_404(Wishlist, product=item_id, user=user)
        wishlist.save()
        
    else:
        Wishlist(user=user, product=product).save() 
    return redirect('wishlist')

@login_required(login_url="/loginUser")
def remove_wishlist_item(request, cart_id):
    if request.method == 'GET':
        item = get_object_or_404(Wishlist, id =cart_id)
        item.delete()
        messages.success(request, "Product removed from Wishlist.")

    return redirect('wishlist')



@login_required(login_url="/loginUser")
def wishlist(request):
    user = request.user
    wishlist = Wishlist.objects.filter(user=user)
    context = {
        'wishlist' : wishlist
    }
    return render(request, 'pages/shop-wishlist.html', context)

def blog(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs' : blogs,
    }
    return render(request, 'pages/blog.html', context)

def blog_details(request,pk):
    recent_blogs = BlogPost.objects.all().order_by('-id')[:5]
    blog_detail = BlogPost.objects.get(pk = pk)
    context = {
        'recent_blogs' : recent_blogs,
        'blog_detail' : blog_detail
        
    }
    return render(request, 'pages/blog-details.html',context)


def compare(request):
    user = request.user
    compare = Compare.objects.filter(user=user).order_by('-id')[:3]
    context = {
        'compare' : compare
    }
    return render(request, 'pages/shop-compare.html', context)

def remove_comp_item(request, cart_id):
    if request.method == 'GET':
        item = get_object_or_404(Compare, id =cart_id)
        item.delete()
        messages.success(request, "Product removed from Compare.")

    return redirect('compare')





# Trial
@login_required(login_url="/loginUser")
def cart_add(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/loginUser")
def item_clear(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/loginUser")
def item_increment(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/loginUser")
def item_decrement(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/loginUser")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/loginUser")
def cart_detail(request):    
    return render(request, 'pages/shop-cart.html')

def thank_you(request):
    return render(request, 'pages/thank-you.html')

def faq(request):
    return render(request,'pages/faq.html')

@login_required(login_url="/loginUser")
def checkout(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id = uid)
        cart = request.session.get('cart')
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        country = request.POST['country']
        region = request.POST['region']
        town = request.POST['town']
        address1 = request.POST['address1']
        phone = request.POST['phone']
        amount = request.POST['amount']
        address2 = request.POST['address2']
        gps_code = request.POST['gps_code']
        order_note = request.POST['order_notes']
        payment = Order(
            user = user,
            first_name = first_name,
            last_name =last_name,
            email = email,
            country = country,
            region = region,
            town = town,
            address1 = address1,
            address2 = address2,
            phone = phone,
            amount = float(amount),
            GPS = gps_code,
            order_note = order_note
        )
        payment.save()
        for i in cart:
            a = cart[i]['quantity']
            b = (int(float(cart[i]['price'])))
            total = a*b
            item = OrderItem(
                 order = payment,
                 product_name = cart[i]['name'],
                 product_image = cart[i]['image'],
                 quantity = cart[i]['quantity'],
                 price = cart[i]['price'],
                 total = total,
            )
            item.save()
        cart.clear()
        context ={
            'payment':payment,
            'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
        }
        return render(request, 'pages/payment.html', context)
        
    return render(request, 'pages/shop-checkout.html')

@login_required(login_url="/loginUser") 
def payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Order, ref = ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Verification Successful')
    else:
        messages.error(request, 'Verification failed. Try again')
    return redirect('checkout')

    
def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            context ={
                'payment':payment,
                'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
            }
            return render(request, 'pages/make_payment.html', context)
    else:
        payment_form = forms.PaymentForm()
        context ={
        'payment_form': payment_form
        }
    return render(request, 'pages/initiate_payment.html', context)


def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref = ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Verification Successful')
    else:
        messages.error(request, 'Verification failed. Try again')
    return redirect('initiate_payment')

