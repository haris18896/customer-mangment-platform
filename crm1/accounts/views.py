from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customre = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='out for delivery').count()
    
    context = {'orders':orders, 'customers':customers, 'total_customre':total_customre,
               'total_orders':total_orders, 'delivered':delivered, 'pending':pending,
               'out_for_delivery':out_for_delivery}

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    
    context = {'products':products,}
    return render(request, 'accounts/products.html',  context)


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request, 'accounts/customer.html',context)


