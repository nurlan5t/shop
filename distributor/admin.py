from django.contrib import admin
from django.utils.html import format_html

from distributor.models import Tag, Category, Product, ProductImage

class ImageInLine(admin.StackedInline):
    model = ProductImage
    extra = 0

class ImageProduct(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="height:50px" />'.format(obj.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    list_display = ['image_tag', ]

class ProductAdmin(admin.ModelAdmin):
    list_display = 'id title text category is_active created updated'.split()
    readonly_fields = 'id created updated'.split()
    search_fields = 'title text'.split()
    list_filter = 'updated category'.split()
    inlines = [ImageInLine]

class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id name text created'.split()

class TagAdmin(admin.ModelAdmin):
    list_display = 'id name text created'.split()



admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage, ImageProduct)
admin.site.register(Product, ProductAdmin)
