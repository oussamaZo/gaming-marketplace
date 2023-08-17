from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from store.controller import authview,cart,wishlist,checkout,order
urlpatterns = [
    
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsview,name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),
    path('register/',authview.register,name="register"),
    path('login/',authview.loginpage,name="loginpage"),
    path('logout/',authview.logoutpage,name="logoutpage"),
    path('add-to-cart',cart.addtocart,name="addtocart"),
    path('cart',cart.viewcart,name="cart"),
    path('update-cart', cart.updatecart, name='updatecart'),
    path('delete-cart-item', cart.deletecartitem, name='deletecartitem'),
    path('wishlist', wishlist.index, name='wishlist'),
    path('add-to-wishlist', wishlist.addtowishlist, name='addtowishlist'),
    path('delete-wishlist-item', wishlist.deleteitem, name='deleteitem'),
    path('checkout', checkout.index, name='checkout'),
    path('place-order', checkout.placeorder, name='placeorder'),
    path('my-orders', order.index,name="myorder"),
    path('view-order/<str:t_no>', order.vieworder,name="orderview"),
    path('product-list', views.productlist),
    path('searchproduct', views.searchh,name="searchproduct"),
    
   


    
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)