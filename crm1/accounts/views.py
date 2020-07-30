from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

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


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print('printing post', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request , pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)






