from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    barcode = models.IntegerField()
    name = models.CharField(max_length=200)
    price_wholesale = models.IntegerField()
    price_retail = models.IntegerField()
    producer = models.CharField(max_length=200)

    def __str__(self):
        return self.name