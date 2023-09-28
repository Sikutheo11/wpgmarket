from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import UserProfile
# from .context_processors import get_cart_counter, get_cart_amounts
from products.models import Category, ProductItem

from vendor.models import Vendor
from django.db.models import Prefetch
# from .models import Cart
# from django.contrib.auth.decorators import login_required
# from django.db.models import Q

# from django.contrib.gis.geos import GEOSGeometry
# from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``
# from django.contrib.gis.db.models.functions import Distance

# from datetime import date, datetime
# from orders.forms import OrderForm


def marketplace(request, category_slug=None):
    categories = None
    products = None
    vendors = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = ProductItem.objects.filter(category=categories, is_available=True)
    else:
        vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)
        products = ProductItem.objects.filter(is_available=True)        
    context = {
        'vendors': vendors,
        'products':products,
        'categories':categories,       
    }
    return render(request, 'marketplace/listings.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = ProductItem.objects.get(category__slug=category_slug, slug=product_slug)        
        # in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    # if request.user.is_authenticated:
    #     try:
    #         orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
    #     except OrderProduct.DoesNotExist:
    #         orderproduct = None
    # else:
    #     orderproduct = None

    # # Get the reviews
    # reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    # # Get the product gallery
    # product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
        'single_product': single_product,
        
    #     'in_cart'       : in_cart,
    #     'orderproduct': orderproduct,
    #     'reviews': reviews,
    #     'product_gallery': product_gallery,
    }    
    return render(request, 'marketplace/product_detail.html', context)


# def category_detail(request,  slug):
#     category = get_object_or_404(Category, slug=slug)

#     vendors = Category.objects.filter(category=category).prefetch_related(
#         Prefetch(
#             'productitems',
#             queryset = ProductItem.objects.filter(is_available=True)
#         )
#     )

#     opening_hours = OpeningHour.objects.filter(vendor=vendor).order_by('day', 'from_hour')
    
#     # Check current day's opening hours.
#     today_date = date.today()
#     today = today_date.isoweekday()
    
#     current_opening_hours = OpeningHour.objects.filter(vendor=vendor, day=today)
#     if request.user.is_authenticated:
#         cart_items = Cart.objects.filter(user=request.user)
#     else:
#         cart_items = None
    # context = {
    #     'vendors': vendors,
    #     'category': category,
#         'cart_items': cart_items,
#         'opening_hours': opening_hours,
#         'current_opening_hours': current_opening_hours,
    # }
    # return render(request, 'marketplace/category_detail.html', context)


# def add_to_cart(request, product_id):
#     if request.user.is_authenticated:
#         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             # Check if the product item exists
#             try:
#                 productitem = ProductItem.objects.get(id=product_id)
#                 # Check if the user has already added that food to the cart
#                 try:
#                     chkCart = Cart.objects.get(user=request.user, productitem=productitem)
#                     # Increase the cart quantity
#                     chkCart.quantity += 1
#                     chkCart.save()
#                     return JsonResponse({'status': 'Success', 'message': 'Increased the cart quantity', 'cart_counter': get_cart_counter(request), 'qty': chkCart.quantity, 'cart_amount': get_cart_amounts(request)})
#                 except:
#                     chkCart = Cart.objects.create(user=request.user, productitem=productitem, quantity=1)
#                     return JsonResponse({'status': 'Success', 'message': 'Added the product to the cart', 'cart_counter': get_cart_counter(request), 'qty': chkCart.quantity, 'cart_amount': get_cart_amounts(request)})
#             except:
#                 return JsonResponse({'status': 'Failed', 'message': 'This product does not exist!'})
#         else:
#             return JsonResponse({'status': 'Failed', 'message': 'Invalid request!'})
        
#     else:
#         return JsonResponse({'status': 'login_required', 'message': 'Please login to continue'})
    


# def decrease_cart(request, food_id):
#     if request.user.is_authenticated:
#         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             # Check if the food item exists
#             try:
#                 fooditem = FoodItem.objects.get(id=food_id)
#                 # Check if the user has already added that food to the cart
#                 try:
#                     chkCart = Cart.objects.get(user=request.user, fooditem=fooditem)
#                     if chkCart.quantity > 1:
#                         # decrease the cart quantity
#                         chkCart.quantity -= 1
#                         chkCart.save()
#                     else:
#                         chkCart.delete()
#                         chkCart.quantity = 0
#                     return JsonResponse({'status': 'Success', 'cart_counter': get_cart_counter(request), 'qty': chkCart.quantity, 'cart_amount': get_cart_amounts(request)})
#                 except:
#                     return JsonResponse({'status': 'Failed', 'message': 'You do not have this item in your cart!'})
#             except:
#                 return JsonResponse({'status': 'Failed', 'message': 'This food does not exist!'})
#         else:
#             return JsonResponse({'status': 'Failed', 'message': 'Invalid request!'})
        
#     else:
#         return JsonResponse({'status': 'login_required', 'message': 'Please login to continue'})


# @login_required(login_url = 'login')
# def cart(request):
#     cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
#     context = {
#         'cart_items': cart_items,
#     }
#     return render(request, 'marketplace/cart.html', context)


# def delete_cart(request, cart_id):
#     if request.user.is_authenticated:
#         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             try:
#                 # Check if the cart item exists
#                 cart_item = Cart.objects.get(user=request.user, id=cart_id)
#                 if cart_item:
#                     cart_item.delete()
#                     return JsonResponse({'status': 'Success', 'message': 'Cart item has been deleted!', 'cart_counter': get_cart_counter(request), 'cart_amount': get_cart_amounts(request)})
#             except:
#                 return JsonResponse({'status': 'Failed', 'message': 'Cart Item does not exist!'})
#         else:
#             return JsonResponse({'status': 'Failed', 'message': 'Invalid request!'})


# def search(request):
#     if not 'address' in request.GET:
#         return redirect('marketplace')
#     else:
#         address = request.GET['address']
#         latitude = request.GET['lat']
#         longitude = request.GET['lng']
#         radius = request.GET['radius']
#         keyword = request.GET['keyword']

#         # get vendor ids that has the food item the user is looking for
#         fetch_vendors_by_fooditems = FoodItem.objects.filter(food_title__icontains=keyword, is_available=True).values_list('vendor', flat=True)
        
#         vendors = Vendor.objects.filter(Q(id__in=fetch_vendors_by_fooditems) | Q(vendor_name__icontains=keyword, is_approved=True, user__is_active=True))
#         if latitude and longitude and radius:
#             pnt = GEOSGeometry('POINT(%s %s)' % (longitude, latitude))

#             vendors = Vendor.objects.filter(Q(id__in=fetch_vendors_by_fooditems) | Q(vendor_name__icontains=keyword, is_approved=True, user__is_active=True),
#             user_profile__location__distance_lte=(pnt, D(km=radius))
#             ).annotate(distance=Distance("user_profile__location", pnt)).order_by("distance")

#             for v in vendors:
#                 v.kms = round(v.distance.km, 1)
#         vendor_count = vendors.count()
#         context = {
#             'vendors': vendors,
#             'vendor_count': vendor_count,
#             'source_location': address,
#         }


#         return render(request, 'marketplace/listings.html', context)


# @login_required(login_url='login')
# def checkout(request):
#     cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
#     cart_count = cart_items.count()
#     if cart_count <= 0:
#         return redirect('marketplace')
    
#     user_profile = UserProfile.objects.get(user=request.user)
#     default_values = {
#         'first_name': request.user.first_name,
#         'last_name': request.user.last_name,
#         'phone': request.user.phone_number,
#         'email': request.user.email,
#         'address': user_profile.address,
#         'country': user_profile.country,
#         'state': user_profile.state,
#         'city': user_profile.city,
#         'pin_code': user_profile.pin_code,
#     }
#     form = OrderForm(initial=default_values)
#     context = {
#         'form': form,
#         'cart_items': cart_items,
#     }
#     return render(request, 'marketplace/checkout.html', context)