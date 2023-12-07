from django.db import models

# Create your models here.
class Lego(models.Model):
  name = models.CharField(max_length=100)
  img_url = models.URLField(max_length=200)
  pieces = models.PositiveIntegerField()
  theme = models.CharField(max_length=100)
  wishlist = models.BooleanField()
  built = models.BooleanField(default=False)
  item_number = models.PositiveBigIntegerField()