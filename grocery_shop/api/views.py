import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from new_shop.models import Category, Item

# Create your views here.
# def products_api(request):
#     products = Item.objects.all()
#     if products.exists():
#         return JsonResponse({})
#     else:
#         return HttpResponse('No products found!')
from django.core.serializers import serialize
from django.http import HttpResponse

def products_api(request):
    products = Item.objects.all().values()

    list_items = list(products)

    data = json.dumps(list_items)
    return HttpResponse(data)


# def django_models_json(request):
#     # Grabs a QuerySet of dicts
#     qs = Post.objects.all().values()

#     # Convert the QuerySet to a List
#     list_of_dicts = list(qs)
    
#     # Convert List of Dicts to JSON
#     data = json.dumps(list_of_dicts)
#     return HttpResponse(data, content_type="application/json")

def categories_api(request):
    categories = Category.objects.all().values('title')

    list_items = list(categories)

    data = json.dumps(list_items)
    return HttpResponse(data)