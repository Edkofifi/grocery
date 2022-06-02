from django import forms

from new_shop.models import Category, Item, Order 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class UpdateItem(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'