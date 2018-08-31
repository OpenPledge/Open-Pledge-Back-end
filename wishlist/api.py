from rest_framework import viewsets, permissions
from .models import WishList, WishListItem, Pledge
from .serializers import WishListSerializer, WishListItemSerializer, PledgeSerializer


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = WishListSerializer


