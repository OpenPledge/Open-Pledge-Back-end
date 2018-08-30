from django.db import models
from open_pledge.users.models import User

# Create your models here.


class WishList(models.Model):
    # id is created by default
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
#    created_at = models.DateTimeField(auto_now_add=True
    def __str__(self):
        return '%s owned by %s' % (self.title, self.owner)


class WishListItem(models.Model):
    wishList = models.ForeignKey(WishList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    needed = models.IntegerField()
    pledged = models.IntegerField()

    def __str__(self):
        return 'WishList - %s - %s %s %s - Needed: %s - Pledged: %s' % (self.wishList, self.name, self.quantity, self.unit, self.needed, self.pledged)

class Pledge(models.Model):
    # id is created by default
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    wishList = models.ForeignKey(WishList, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.wishList, self.owner)
