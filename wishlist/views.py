from django.shortcuts import render
from wishlist.models import Wishlist
from wishlist.models import Pledge
from django.forms import ModelForm
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

# Create your views here.
@ensure_csrf_cookie

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['data', 'owner_id']


class PledgeForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['data', 'owner_id']

# Wishlist CRUD API operations
# get_wishlists: returns all of the user's wishlists based on user ID
# get_wishlist: returns a specific wishlist based on wishlist ID
# new_wishlist: creates a new wishlist based on user ID, owned by that user
# update_wishlist: updates a wishlist based on a specific wishlist ID 
# delete_wishlist: deletes a wishlist based on a specific wishlist ID 

def get_wishlists(request, userId):
    my_wishlist = Wishlist.objects.get(owner_id=userId).data
    return JsonResponse({
        "data": my_wishlist,
    })


def get_wishlist(request, wishlistId):
    my_wishlist = Wishlist.objects.get(id=wishlistId).data
    return JsonResponse({
        "data": my_wishlist,
    })


def new_wishlist(request, userId):

    if request.method == "POST":
        input_data = json.dumps(request.body, seperators=(',', ':'))
        my_wishlist = Wishlist(input_data, userId)
        my_wishlist.save()
        print(my_wishlist)


def update_wishlist(request, wishlistId):
    input_data = json.dumps(request.body, seperators=(',', ':'))
    my_wishlist = Wishlist.objects.get(id=wishlistId)
    my_wishlist.update(data=input_data)
    print('updated wishlist', my_wishlist)


def remove_wishlist(request, wishlistId):
    my_wishlist = Wishlist.objects.filter(id=wishlistId)
    print('deleting wishlist', my_wishlist)
    my_wishlist.delete()


# Pledge CRUD API Operations
# get_pledges: returns all of the user's pledges based on user ID
# get_pledge: returns a specific pledge based on pledge ID
# new_pledge: creates a new pledge based on user ID, owned by that user
# update_pledge: updates a pledge based on a specific pledge ID 
# delete_pledge: deletes a pledge based on a specific pledge ID

def get_pledges(request, userId):
    my_pledge = Pledge.objects.get(owner_id=userId).data
    return JsonResponse({
        "data": my_pledge
    })


def get_pledge(request, pledgeId):
    my_pledge = Pledge.objects.get(id=pledgeId).data
    return JsonResponse({
        "data": my_pledge
    })


def new_pledge(request, userId):
    if request.method == "POST":
        input_data = json.dumps(request.body, seperators=(',', ':'))
        my_pledge = Pledge(input_data, userId)
        my_pledge.save()
        print('created pledge', my_pledge)


def update_pledge(request, pledgeId):
    input_data = json.dumps(request.body, seperators=(',', ':'))
    my_pledge = Pledge.objects.get(id=pledgeId)
    my_pledge.update(data=input_data)
    print('updated pledge', my_pledge)


def remove_pledge(request, pledgeId):
    my_pledge = Pledge.objects.filter(id=pledgeId)
    print('deleting pledge', my_pledge)
    my_pledge.delete()
