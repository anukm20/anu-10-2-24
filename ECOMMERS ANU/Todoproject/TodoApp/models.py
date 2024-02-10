from django.db import models

# Create your models here.
class cart(models.Model):
    price=models.IntegerField()
    brand=models.TextField()
    image=models.CharField(max_length=400)
    product_name=models.CharField(max_length=200)