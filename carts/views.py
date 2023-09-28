from django.shortcuts import render
from .models import Cart

# Create your views here.
# @login_required(login_url = 'login')
def cart(request):
    # cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
    # context = {
    #     'cart_items': cart_items,
    # }
    return render(request, 'marketplace/cart.html')