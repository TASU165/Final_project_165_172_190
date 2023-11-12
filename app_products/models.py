from django.db import models
from django.utils.html import format_html

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): 
        return self.name

class Product(models.Model):
    code= models.CharField(max_length=10, unique=True)
    slug= models. SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete = models.CASCADE)
    image = models.FileField(upload_to='upload', null=True, blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def show_image(self):
        if self.image:
            return format_html('<img src="%s" height = "50px">' % self.image.url)
        return ''
    show_image.allow_tags = True

class ProductComment (models.Model):
    product= models.ForeignKey(Product, on_delete = models.CASCADE)
    comment = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.comment