
from django.shortcuts import render
from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import BarcodeSerializer
from .models import Product

# Create your views here.



class barcode(ListCreateAPIView):
    serializer_class=BarcodeSerializer
    queryset=Product.objects.all()
    


class bar_code(RetrieveUpdateDestroyAPIView):
    serializer_class=BarcodeSerializer
    queryset=Product.objects.all()