from django.contrib import admin
from .models import WishList
from .models import WishListItem
from .models import Pledge

# Register your models here.
admin.site.register(WishList)
admin.site.register(WishListItem)
admin.site.register(Pledge)
