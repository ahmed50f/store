from rest_framework import serializers
from .models import Category, Product, Rating, Order, CartItem, Cart


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_date',)

    def validate(self, data):
        product = data.get('product')
        quantity = data.get('quantity')

        if not product:
            raise serializers.ValidationError({'product': 'يجب اختيار المنتج.'})
        if not quantity or int(quantity) < 1:
            raise serializers.ValidationError({'quantity': 'يجب أن تكون الكمية 1 على الأقل.'})
        if quantity > product.quantity:
            raise serializers.ValidationError({
                'quantity': 'الكمية المطلوبة أكبر من المتاحة في المخزون. المتاح: {}'.format(product.quantity)
            })
        return data


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ('user',)
