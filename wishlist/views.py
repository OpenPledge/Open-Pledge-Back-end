from django.shortcuts import render
from wishlist.models import WishList
from wishlist.models import WishListItem
from wishlist.models import Pledge
from django.forms import ModelForm
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

# Create your views here.


class WishListForm(ModelForm):
    class Meta:
        model = WishList
        fields = ['owner', 'title']


class WishListItemForm(ModelForm):
    class Meta:
        model = WishListItem
        fields = ['wishList', 'name', 'quantity', 'unit', 'needed', 'pledged']


class PledgeForm(ModelForm):
    class Meta:
        model = Pledge
        fields = ['owner', 'wishList']

# WishList CRUD API operations
# get_wish_list_ids: returns all of the user's wishLists based on user ID
# get_wishList: returns a specific wishList based on wishList ID
# get_wishListItems: returns all items for a specified wishlist
# new_wish_list: creates a new wishList based on user ID, owned by that user
# update_wish_list: updates a wishList based on a specific wishList ID
# delete_wishList: deletes a wishList based on a specific wishList ID 


def get_wish_list_ids(request, userId):
    wish_list_ids = WishList.objects.filter(owner_id=userId).values_list('id', flat=True).order_by('id')

    return JsonResponse({
        "data": wish_list_ids,
    })


def get_wish_list_items(request, wishListId):
    my_wish_list = WishList.objects.get(id=wishListId)
    my_wish_list_as_dicts = my_wish_list.values('name', 'quantity', 'unit', 'needed', 'pledged')
    return JsonResponse({
        "data": my_wish_list_as_dicts,
    })


def new_wish_list(request, userId):
    if request.method == "POST":
        input_data = json.dumps(request.body, seperators=(',', ':'))
        my_wishList = WishList(input_data.title, userId)
        my_wishList.save()
        print(my_wishList)


def update_wish_list(request, wishListId):
    input_data = json.dumps(request.body, seperators=(',', ':'))
    my_wishList = WishList.objects.get(id=wishListId)
    my_wishList.name = input_data.name
    my_wishList.quantity = input_data.quantity
    my_wishList.unit = input_data.unit
    my_wishList.needed = input_data.needed
    my_wishList.pledged = input_data.pledged
    my_wishList.save()
    print('updated wishList', my_wishList)


def remove_wish_list(request, wishListId):
    my_wishList = WishList.objects.filter(id=wishListId)
    print('deleting wishList', my_wishList)
    my_wishList.delete()


# Pledge CRUD API Operations
# get_pledges: returns all of the user's pledges based on user ID
# get_pledge: returns a specific pledge based on pledge ID
# new_pledge: creates a new pledge based on user ID, owned by that user
# update_pledge: updates a pledge based on a specific pledge ID 
# delete_pledge: deletes a pledge based on a specific pledge ID

def get_pledges_by_user(request, userId):
    my_pledges = Pledge.objects.filter(owner_id=userId).data
    return JsonResponse({
        "data": my_pledges
    })


def get_pledges_by_wish_list(request, wishListId):
    wishList_pledges = Pledge.objects.filter(wish_list=wishListId).data
    return JsonResponse({
        "data": wishList_pledges
    })


def get_pledge(request, pledgeId):
    the_pledge = Pledge.objects.get(id=pledgeId).data
    return JsonResponse({
        "data": the_pledge
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
