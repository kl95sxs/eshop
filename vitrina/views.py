from django.shortcuts import render, get_object_or_404
from .models import Product

def vitrina (request):
    Products = Product.objects.all()
    return render(request, 'vitrina/vitrina.html', {'Products': Products})
def detail (request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render (request, 'vitrina/detail.html', {'product': product})
