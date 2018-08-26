from django.db import models

# Create your models here.
class Wishlist(models.Model):
    item = models.CharField(max_length=200)
    par = models.IntegerField(default=0)
#    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.item, self.par)
