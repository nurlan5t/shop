from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from  .serializers import ProductSerializer, CategorySerializer, TagNameSerializer
from distributor.models import Product, Tag, Category
from rest_framework.decorators import api_view

class ListCreateProductAPI(APIView, PageNumberPagination):
    allowed_methods = ['get', 'post']
    def get(self, request):
        search_word = request.query_params.get('search_word', '')
        # category_id = request.query_params.get('category')
        products = Product.objects.filter(Q(title__icontains=search_word) | Q(text__icontains=search_word))
                                          # category_id=category_id))
        # data = ProductSerializer(products, many=True).data
        results = self.paginate_queryset(products, request, view=self)
        return self.get_paginated_response(ProductSerializer(results, many=True).data)

    def post(self, request):
        title = request.data.get('title')
        text = request.data.get('text')
        category_id = int(request.data.get('category_id'))
        product = Product.objects.create(title=title, text=text, category_id=category_id)
        product.save()
        return Response(status=status.HTTP_200_OK, data=ProductSerializer(product).data)

class ListCreateCategoryAPI(APIView):
    allowed_methods = ['get', 'post']
    def get(self, request):
        categorys = Category.objects.all()
        data = CategorySerializer(categorys, many=True).data
        return Response(data=data)
    def post(self, request):
        name = request.data.get('name')
        text = request.data.get('text')
        category = Category.objects.create(name=name, text=text)
        category.save()
        return Response(status=status.HTTP_200_OK, data=CategorySerializer(category).data)

class ListCreateTagAPI(APIView):
    allowed_methods = ['get', 'post']
    def get(self, request):
        tags = Tag.objects.all()
        data = TagNameSerializer(tags, many=True).data
        return Response(data=data)
    def post(self, request):
        name = request.data.get('name')
        text = request.data.get('text')
        tag = Tag.objects.create(name=name, text=text)
        tag.save()
        return Response(status=status.HTTP_200_OK, data=CategorySerializer(tag).data)

# @api_view(['GET', 'POST'])
# def get_drf_products(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         data = ProductSerializer(products, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         title = request.data.get('title')
#         text = request.data.get('text')
#         category_id = int(request.data.get('category_id'))
#         product = Product.objects.create(title=title, text=text, category_id=category_id)
#         product.save()
#         return Response(status=status.HTTP_200_OK, data=ProductSerializer(product).data)

# @api_view(['GET', 'POST'])
# def new_category(request):
#     if request.method == 'GET':
#         categorys = Category.objects.all()
#         data = CategorySerializer(categorys, many=True).data
#         return Response(data=data)
#
#     elif request.method == 'POST':
#         name = request.data.get('name')
#         text = request.data.get('text')
#         category = Category.objects.create(name=name, text=text)
#         category.save()
#         return Response(status=status.HTTP_200_OK, data=CategorySerializer(category).data)

@api_view(['GET', 'POST'])
def new_tag(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        data = TagNameSerializer(tags, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        name = request.data.get('name')
        text = request.data.get('text')
        tag = Tag.objects.create(name=name, text=text)
        tag.save()
        return Response(status=status.HTTP_200_OK, data=CategorySerializer(tag).data)
