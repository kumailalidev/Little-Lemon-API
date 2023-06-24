from rest_framework import serializers

from django.contrib.auth.models import User

from .models import (
    Category,
    MenuItem,
    Cart,
    Order,
    OrderItem,
)


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for categories."""

    class Meta:
        model = Category
        fields = ["id", "title", "slug"]


class MenuItemSerializer(serializers.ModelSerializer):
    """Serializer for menu items."""

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "category", "featured"]


class CartSerializer(serializers.ModelSerializer):
    """Serializer for cart item"""

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    def validate(self, attrs):
        attrs["price"] = attrs["quantity"] * attrs["unit_price"]
        return attrs

    class Meta:
        model = Cart
        fields = ["user", "menuitem", "unit_price", "quantity", "price"]
        extra_kwargs = {"price": {"read_only": True}}


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for order item."""

    class Meta:
        model = OrderItem
        fields = ["order", "menuitem", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for order."""

    orderitem = OrderItemSerializer(many=True, read_only=True, source="order")

    class Meta:
        model = Order
        fields = ["id", "user", "delivery_crew", "status", "date", "total", "orderitem"]
