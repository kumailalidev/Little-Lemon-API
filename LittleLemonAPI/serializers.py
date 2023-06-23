from rest_framework import serializers

from .models import Category, MenuItem


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
