from django.shortcuts import render
from rest_framework.response import Response
from  .serializers import ProductSerializer
from distributor.models import Product, Tag
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_drf_products(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)
