from .models import (
    Category,
    MenuItem,
    Cart,
)
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer

from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework.response import Response


class CategoriesView(generics.ListCreateAPIView):
    """View for displaying categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class MenuItemsView(generics.ListCreateAPIView):
    """View for displaying menu items."""

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ["category__title"]
    ordering_fields = ["price", "inventory"]

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """View for displaying, updating, and deleting single menu item."""

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class CartView(generics.ListCreateAPIView):
    """View for viewing cart items, adding items to cart and deleting items from cart."""

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    # GET Method
    def get_queryset(self):
        return Cart.objects.all().filter(user=self.request.user)

    # DELETE Method
    def delete(self, request, *args, **kwargs):
        Cart.objects.all().filter(user=self.request.user).delete()
        return Response("OK: Items deleted from cart.")
