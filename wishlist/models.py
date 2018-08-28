from django.db import models
from open_pledge.users.models import User

# Create your models here.


class Wishlist(models.Model):
    # id is created by default
    data = models.CharField(max_length=1800)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

#    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s owned by %s' % (self.data, self.owner)


class Pledge(models.Model):
    # id is created by default
    data = models.CharField(max_length=1800)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s owned by %s' % (self.data, self.owner)
