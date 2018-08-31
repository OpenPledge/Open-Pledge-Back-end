from django.shortcuts import render
from wishlist.models import WishList
from wishlist.models import WishListItem
from wishlist.models import Pledge
from django.forms import ModelForm
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.


class WishListForm(ModelForm):
    class Meta:
        model = WishList
        fields = ['owner', 'title']


class WishListItemForm(ModelForm):
    class Meta:
        model = WishListItem
        fields = ['wish_list', 'name', 'unit', 'needed', 'pledged']


class PledgeForm(ModelForm):
    class Meta:
        model = Pledge
        fields = ['owner', 'wish_list']

# WishList CRUD API operations
# get_wish_list_ids: returns all of the user's wishLists based on user ID
# get_wishList: returns a specific wishList based on wishList ID
# get_wishListItems: returns all items for a specified wishList
# new_wish_list: creates a new wishList based on user ID, owned by that user
# update_wish_list: updates a wishList based on a specific wishList ID
# delete_wishList: deletes a wishList based on a specific wishList ID 


def get_user_info(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "user_id": request.user.id,
        })
    else:
        return JsonResponse({
            "error": "You ain't logged in."
        })


def get_wish_list_ids(request, user_id):
    wish_list_ids = WishList.objects.filter(owner_id=user_id).values_list('id', flat=True).order_by('id')

    return JsonResponse({
        "data": wish_list_ids,
    })


def get_all_wish_lists(request):
    wish_lists = list(WishList.objects.all().values('title', 'id'))
    return JsonResponse({
        "data": wish_lists
    })


def get_wish_list_items(request, wish_list_id):
    items = WishListItem.objects.filter(wish_list_id=wish_list_id)
    items_list = list(items.values('name', 'unit', 'needed', 'pledged'))
    print(items_list)
    return JsonResponse({
        "data": items_list,
    })


def new_wish_list_item(request, wish_list_id):
    if request.method == "POST":
        input_data = json.dumps(request.body, seperators=(',', ':'))
        print(input_data)
        item = WishListItem(
            wish_list_id,
            input_data.name,
            input_data.unit,
            input_data.needed,
            input_data.pledged)
        item.save()


def new_wish_list(request, user_id):
    if request.method == "POST":
        input_data = json.dumps(request.body, seperators=(',', ':'))
        my_wish_list = WishList(input_data.title, user_id)
        my_wish_list.save()
        print(my_wish_list)


def update_wish_list(request, wish_list_id):
    input_data = json.dumps(request.body, seperators=(',', ':'))
    my_wish_list = WishList.objects.get(id=wish_list_id)
    my_wish_list.name = input_data.name
    my_wish_list.unit = input_data.unit
    my_wish_list.needed = input_data.needed
    my_wish_list.pledged = input_data.pledged
    my_wish_list.save()
    print('updated wishList', my_wish_list)


def remove_wish_list(request, wish_list_id):
    my_wish_list = WishList.objects.filter(id=wish_list_id)
    print('deleting wishList', my_wish_list)
    my_wish_list.delete()


# Pledge CRUD API Operations
# get_pledges: returns all of the user's pledges based on user ID
# get_pledge: returns a specific pledge based on pledge ID
# new_pledge: creates a new pledge based on user ID, owned by that user
# update_pledge: updates a pledge based on a specific pledge ID 
# delete_pledge: deletes a pledge based on a specific pledge ID

def get_pledges_by_user(request, user_id):
    my_pledges = Pledge.objects.filter(owner_id=user_id).data
    return JsonResponse({
        "data": my_pledges
    })


def get_pledges_by_wish_list(request, wish_list_id):
    wishList_pledges = Pledge.objects.filter(wish_list=wish_list_id).data
    return JsonResponse({
        "data": wishList_pledges
    })


def get_pledge(request, pledgeId):
    the_pledge = Pledge.objects.get(id=pledgeId).data
    return JsonResponse({
        "data": the_pledge
    })


def new_pledge(request, user_id):
    if request.method == "POST":
        input_data = json.dumps(request.body, seperators=(',', ':'))
        my_pledge = Pledge(input_data, user_id)
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
