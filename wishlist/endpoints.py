from django.conf.urls import include, url
from rest_framework import routers

from .api import WishListViewSet

router = routers.DefaultRouter()
router.register('wishlist', WishListViewSet)

urlpatterns = [
    url("^", include(router.urls)),
]
