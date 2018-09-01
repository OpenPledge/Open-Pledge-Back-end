# todos/serializers.py
from rest_framework import serializers
from .models import WishList
from .models import WishListItem
from .models import Pledge


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['owner', 'title']


class WishListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        fields = ['wish_list', 'name', 'unit', 'needed', 'pledged']


class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['owner', 'wish_list']
