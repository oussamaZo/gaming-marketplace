from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import Product,Cart,Order,OrderItem
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    orders = Order.objects.filter(user=request.user)
    
    # Get a list of tracking numbers for orders that have a message from the seller
    orders_with_message = Order.objects.filter(user=request.user, message__isnull=False)
    orders_with_message_tracking_numbers = [order.tracking_no for order in orders_with_message]
    
    context = {
        'orders': orders,
        'orders_with_message_tracking_numbers': orders_with_message_tracking_numbers,
    }
    
    return render(request, "store/orders/index.html", context)
def vieworder(request, t_no):
    orders = Order.objects.filter(tracking_no=t_no, user=request.user).first()
    orderitems = orders.orderitem_set.all() if orders else None

    # Check if the user is logged in and if the order has a message
    message_for_user = None
    if request.user.is_authenticated and orders.message:
        message_for_user = orders.message

    context = {
        'orders': orders,
        'orderitems': orderitems,
        'message_for_user': message_for_user,
    }
    return render(request, "store/orders/view.html", context)