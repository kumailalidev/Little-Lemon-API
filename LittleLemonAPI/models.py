from django.db import models


class Category(models.Model):
    """Product category."""

    slug = models.SlugField()
    title = models.CharField(max_length=255)


class MenuItem(models.Model):
    """Menu item"""

    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
