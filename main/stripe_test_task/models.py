from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    price = models.FloatField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
