# product/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    version = models.IntegerField(default=0)  # Version field for optimistic locking

    def save(self, *args, **kwargs):
        if self.pk:  # If updating an existing record, increment version
            self.version += 1
        super(Product, self).save(*args, **kwargs)
