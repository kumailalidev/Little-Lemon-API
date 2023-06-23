from django.urls import path
from LittleLemonAPI import views

urlpatterns = [
    path("categories/", views.CategoriesView.as_view(), name="categories"),
    path("menu-items/", views.MenuItemsView.as_view(), name="menu_items"),
]
