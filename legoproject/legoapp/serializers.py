from .models import Lego
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class LegoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Lego
    fields = ['id', 'name', 'img_url', 'pieces', 'theme', 'wishlist', 'built', 'item_number']
