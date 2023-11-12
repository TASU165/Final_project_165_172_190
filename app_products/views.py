from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from slugify import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category, Product
from .forms import ProductForm

# Create your views here.
def products(request):
    categoryes = Category.objects.all()
    productes = Product.objects.filter(published = True)

    categ_id = request.GET.get('categoryid')
    if categ_id:
        productes = productes.filter(category_id = categ_id)

    paginator = Paginator(productes, 6)
    page = request.GET.get('page')
    try:
        productes = paginator.page(page)
    except PageNotAnInteger:
        productes = paginator.page(1)
    except EmptyPage:
        productes = paginator.page(paginator.num.pages)
    
    
    
    return render(request, 'app_products/products.html',{
        'categoryes': categoryes,
        'productes': productes,
        'categ_id' : categ_id,
    })


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'app_products/detail.html',{
        'product': product, 
    })

def product_add(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.published= True
            product.save()
            form.save_m2m()
            messages.success(request, 'Save success')
            return HttpResponseRedirect(reverse('products', kwargs={}))
        messages.error(request, 'Save failed!')
    return render(request, 'app_products/add.html', { 
        'form': form,
    })

def cart_add(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_items = request.session.get('cart_items') or []

    # update existing item

    duplicated = False
    for c in  cart_items:
        if c.get('slug') == product.slug:
            c['qty'] = int(c.get('qty') or '0') + 1
            duplicated = True


    if not duplicated:
        cart_items.append({
            'id': product.id,
            'slug': product.slug,
            'name': product.name,
            'price': 0,
            'qty': 1,
        })

    for d in cart_items:
        if d.get('slug') == product.slug:
            d['price'] = int(d.get('price') ) + product.price

    request.session['cart_items'] = cart_items
    return HttpResponseRedirect(reverse('cart_list',kwargs={}))

def cart_list(request):
    cart_items = request.session.get('cart_items') or []

    total_qty = 0 
    for c in cart_items:
        total_qty = total_qty + c.get('qty')

    request.session['cart_qty'] = total_qty

    total_price = 0
    for c in cart_items:
        total_price = total_price + c['price']

    request.session['total_price'] = total_price
    
    return render(request, 'app_products/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

    
def delete_all(request):
    request.session['cart_items'] = []
    request.session.clear()

    return render(request, 'app_products/cart.html', {
        'success': 'ลบสินค้าทั้งหมดเรียบร้อย',
    })


def cart_delete(request, slug):
    cart_items = request.session.get('cart_items') or []

    for i in range(len(cart_items)):
        if cart_items[i]['slug'] == slug:
            del cart_items[i]
            break

    request.session['cart_items'] = cart_items
    return HttpResponseRedirect(reverse('cart_list', kwargs={}))

def cart_reduce(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_items = request.session.get('cart_items') or []
    

    duplicated = False
    for c in cart_items:
        if c.get('slug') == product.slug:
            c['qty'] = int(c.get('qty') or '0') - 1
            duplicated = True
        
    if not duplicated:
        cart_items.append({
            'id': product.id,
            'slug': product.slug,
            'name': product.name,
            'price':0,
            'qty': 0,
        })
    

    for d in cart_items:
        if d.get('slug') == product.slug:
            d['price'] = int(d.get('price') ) - product.price
            
        

    request.session['cart_items'] = cart_items
    return HttpResponseRedirect(reverse('cart_list', kwargs={}))

