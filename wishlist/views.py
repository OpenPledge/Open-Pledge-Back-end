from django.shortcuts import render
from wishlist.models import Wishlist
from django.forms import ModelForm
from django.http import JsonResponse
# Create your views here.


class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['item', 'par']


def get_wishlist(request):
    id = 0
    my_wishlist = Wishlist.objects.get(par=id).item
    return JsonResponse({
        "data": my_wishlist,
    })


def new_wishlist(request):
    print(request)



