from django import forms

from new_shop.models import Item, Order 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class UpdateItem(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']