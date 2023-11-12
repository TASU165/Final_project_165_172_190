from django.contrib import admin
from .models import Category, Product, ProductComment

class ProductCommentTabularInline(admin.TabularInline):
    model = ProductComment
    extra = 0

class ProductAdmin (admin. ModelAdmin):
    list_display = ['code', 'name', 'category', 'price', 'published','show_image' ]
    list_filter = ['published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug':['name']}
    fieldsets =(
        (   None, {'fields': ['code', 'slug', 'name', 'description', 'price','image','published']}), 
        ('Category', {'fields': ['category']})
                                                                                                             
    )

    inlines = [ProductCommentTabularInline]



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# Register your models here.
