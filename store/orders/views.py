from django.shortcuts import render

def order(request):
    return render(request, 'orders/order.html')

def orders_list(request):
    return render(request, 'orders/orders.html')

def order_create(request):
    return render(request, 'orders/order_create.html')

def success(request):
    return render(request, 'orders/success.html')
