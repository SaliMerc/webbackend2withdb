from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_category=models.CharField(max_length=50)
    product_price=models.FloatField(blank=False)
    product_qty=models.IntegerField(blank=False)
    product_image=models.ImageField(upload_to='products/')
    product_description=models.TextField()

    def __str__(self):
        return self.product_name
