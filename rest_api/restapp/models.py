from django.db import models

class Product(models.Model):
    name = models.CharField( max_length=250)
    price = models.FloatField(default = 0)
    created_at = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.name