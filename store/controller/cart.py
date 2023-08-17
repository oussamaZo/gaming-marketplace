from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import Product,Cart
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

def addtocart(request):
    if request.method == 'POST' :
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"Product Already in cart "})   
                else:
                    prod_qty=int(request.POST.get('prodqan'))
                    if product_check.quantity>=prod_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty )
                        return JsonResponse({'status':"Product added successfully"})    
                    else:
                        return JsonResponse({'status':" Only "+ str(product_check.quantity)+" quantity available"})



            else:
                return JsonResponse({'status':"No such Product found"})    
        else:
            return JsonResponse({'status':"Login to Continue"})  
    return redirect('/')     


@login_required(login_url='loginpage')
def viewcart(request):
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,"store/cart.html",context)

def checkout_view(request):
    # Your checkout view logic goes here
    return render(request, 'store/checkout.html')


def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart=Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty=prod_qty
            cart.save()
            return JsonResponse({'status':"Updated Successfully"})
    return redirect("/")    

def deletecartitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            try:
                cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
                cartitem.delete()

                # Check if the cart is empty after deletion
                is_empty = not Cart.objects.filter(user=request.user).exists()

                return JsonResponse({'status': "Deleted Successfully", 'is_empty': is_empty})
            except Cart.DoesNotExist:
                return JsonResponse({'status': "Product not found in cart"})
        else:
            return JsonResponse({'status': "Login to continue"})

    return redirect("/")
