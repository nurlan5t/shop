from rest_framework import serializers
from .models import Product, Tag, Category

class TagNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'id name text created'.split()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name text created'.split()


class ProductSerializer(serializers.ModelSerializer):
    tags = TagNameSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id title category text is_active created updated tags'.split()

    category = serializers.SerializerMethodField()
    def get_category(self, obj):
        return obj.category.name