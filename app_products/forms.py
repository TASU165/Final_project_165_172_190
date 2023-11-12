from django import forms 
from .models import Product
class ProductForm(forms. ModelForm):
    class Meta:
        model = Product
        exclude = ['id', 'slug', 'published', 'created', 'updated']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['code'].error_messages = {
            'required': 'Please enter product code',
        }
        self.fields['name'].error_messages = {
            'required': 'Please enter product name', 
        }
        self.fields['price'].error_messages = {
            'required': 'Please enter product price',
        }

    def clean(self):
        cd = super(ProductForm, self).clean()
        if not cd.get('category'):
            self.add_error('category', 'Please select category name')