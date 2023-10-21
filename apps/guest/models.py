from django.db import models

class Guest(models.Model):
    first_name = models.CharField('First Name',max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name