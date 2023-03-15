from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    isPriority = models.BooleanField(default=False, blank=True, null=True)


def __str__(self):
    return f"{self.title} {self.image_url} {self.price} {self.description} {self.isPriority}"
