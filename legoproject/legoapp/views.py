from django.shortcuts import render

# Create your views here.
from .models import Lego
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LegoSerializer

class LegoViewSet(viewsets.ModelViewSet):
  queryset = Lego.objects.all()
  serializer_class = LegoSerializer
  permission_classes = [permissions.AllowAny]