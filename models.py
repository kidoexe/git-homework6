from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=99999,decimal_places=1)
    stock = models.IntegerField()

