from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    product_des = models.CharField(max_length=80)
    product_date = models.DateField()
