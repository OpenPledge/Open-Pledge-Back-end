from django.shortcuts import render
from wishlist.models import Wishlist
from django.forms import ModelForm
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@ensure_csrf_cookie

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['data']


def get_wishlist(request, userId):
    my_wishlist = Wishlist.objects.get(owner_id=userId).data
    return JsonResponse({
        "data": my_wishlist,
    })


def new_wishlist(request, userId):

    if request.method == "POST":
        input_data = json.dumps(request.body, seperators=(',',':'))
        my_wishlist = Wishlist(input_data)
        my_wishlist.save()
        print(my_wishlist)




