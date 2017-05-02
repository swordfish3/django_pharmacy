from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from cart.cart import Cart
from .models import Product

@login_required

def index(request):
    return HttpResponse("Hello, world. You're at the pharmacy_app index.")



def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
    return render_to_response('cart.html', dict(cart=Cart(request)))
