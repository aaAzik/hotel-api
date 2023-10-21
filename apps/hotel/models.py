from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    rating = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.name
