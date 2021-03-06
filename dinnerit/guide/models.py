from django.db import models

class Dish(models.Model):
    
    dish_name = models.CharField(
        max_length=255,
    )
    cuisine = models.CharField(
        max_length=255,
    )
    
    
    def __str__(self):
        return ' -- '.join([
            self.dish_name,
            self.cuisine,
        ])
