from django.db import models

# Create your models here.

class Buyer(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
