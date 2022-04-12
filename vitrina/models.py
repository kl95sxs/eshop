from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'vitrina/images')
    url = models.URLField(blank=True)
    in_cart = models.BooleanField()

    def __str__(self):
        return self.title
