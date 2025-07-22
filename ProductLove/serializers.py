from rest_framework import serializers
from .models import ProductLove


class ProductLoveSerializer(serializers.ModelSerializer):
    love_count = serializers.SerializerMethodField()
    class Meta:
        model = ProductLove
        fields = ['id', 'user', 'product', 'love_count', 'created']
        

    def get_love_count(self, obj):
            return ProductLove.objects.filter(product=obj.product).count()