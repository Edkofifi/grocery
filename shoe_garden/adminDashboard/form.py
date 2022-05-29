from django import forms

from new_shop.models import Item 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'