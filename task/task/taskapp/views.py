from django.shortcuts import render
from rest_framework import generics
from .models import *
from . import serializers
# Create your views here.

class makedetails(generics.ListCreateAPIView):
    queryset = newtask.objects.all()
    serializer_class = serializers.taskserializers

class removedetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = newtask.objects.all()
    serializer_class = serializers.taskserializers