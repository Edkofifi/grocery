from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from adminDashboard.form import ProductForm

from new_shop.models import Item

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Username or Password is incorrect')
        else:
            messages.error(request, 'All fields must be filled!!')
    return render(request, 'admin_dashboard2/sign-in.html')

def admin_logout(request):
    logout(request)
    return render(request,'dashboard/login.html')


def dashboard(request):
    return render(request, 'base/basefile.html')

def profile(request):
    return render(request, 'dashboard/back-end/profile.html')

def vendor_list(request):
    return render(request, 'dashboard/back-end/list-vendor.html')

def create_vendor(request):
    return render(request, 'dashboard/back-end/create-vendor.html')


def coupon_list(request):
    return render(request, 'dashboard/back-end/coupon-list.html')

def create_coupon(request):
    return render(request, 'dashboard/back-end/create-coupon.html')


def user_list(request):
    return render(request, 'dashboard/back-end/user-list.html')

def create_user(request):
    return render(request, 'dashboard/back-end/create-user.html')


def category_main(request):
    return render(request, 'dashboard/back-end/main-category.html')

def category_sub(request):
    return render(request, 'dashboard/back-end/sub-category.html')


def product_list(request):
    products = Item.objects.all()

    context={'products': products }
    return render(request, 'admin_dashboard/products.html', context)



def product_add(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = ProductForm()
        else:
            product = Item.objects.get(pk =id)
            form = ProductForm(instance = product)
        return render(request, 'admin_dashboard/add_product.html', {'form':form})
    else:
        if id==0:
            form = ProductForm(request.POST, request.FILES)
        else:
            product = Item.objects.get(pk=id)
            form = ProductForm(request.POST, product, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('product_list')
    

def orders(request):
    return render(request, 'admin_dashboard/orderlist.html')

def invoice(request):
    return render(request, 'dashboard/back-end/invoice.html')


def statistics(request):
    return render(request, 'admin_dashboard/statistics.html')

def reports(request):
    return render(request, 'dashboard/back-end/reports.html')
