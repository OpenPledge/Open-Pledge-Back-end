from django.shortcuts import render

# Create your views here.
def get_wishlist(request):
    my_wishlist = Wishlist.objects.all()
    my_wishlists_as_dicts = my_wishlist.values('item', 'par')
    return JsonResponse({
        "data": my_wishlists_as_dicts,
    })
