from django.db import models


# Create your models here.
class Product(models.Model):
    CATEGORY = [
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables')
    ]

    PRDName = models.CharField(max_length=30, verbose_name=("Product Name"))
    PRDDesc = models.TextField(verbose_name=("Product Description"))
    PRDImage = models.ImageField(
        upload_to="photos/", verbose_name=("Image"), blank=True, null=True)
    PRDQuantity = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name=("Quantity"))
    PRDPrice = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name=("Price"))
    PRDCategory = models.CharField(
        max_length=15, null=True, choices=CATEGORY, verbose_name=("Categories"))

    def __str__(self):
        return self.PRDPrice

    class Meta:
        ordering = ['-PRDPrice']


class UserOrder(models.Model):
    onions = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    potatos = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    carrots = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return "Order Number " + str(self.pk)
