from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import Product,Cart
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from store.models import Wishlist
@login_required(login_url='loginpage')
def index(request):
    wishlist=Wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlist}
    return render(request,'store/wishlist.html',context)

def addtowishlist(request):
    if request.method == 'POST' :
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status':"Product Already in Wishlist "})   
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':"Product added to Wishlist"})

                    

            else:
                return JsonResponse({'status':"No such Product found"})    
        else:
            return JsonResponse({'status':"Login to Continue"})  
    return redirect('/')     
def deleteitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            try:
                wishlistitem = Wishlist.objects.get(user=request.user, product_id=prod_id)
                wishlistitem.delete()

                # Check if the wishlist is empty after deletion
                is_empty = not Wishlist.objects.filter(user=request.user).exists()

                return JsonResponse({'status': "Product Removed from Wishlist", 'is_empty': is_empty})
            except Wishlist.DoesNotExist:
                return JsonResponse({'status': "Product not found in wishlist"})
        else:
            return JsonResponse({'status': "Login to continue"})

    return redirect("/")