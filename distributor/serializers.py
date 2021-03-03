from rest_framework import serializers
from .models import Product, Tag

class TagNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'name'.split()


class ProductSerializer(serializers.ModelSerializer):
    tags = TagNameSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id title category tags'.split()

    category = serializers.SerializerMethodField()
    def get_category(self, obj):
        return obj.category.name