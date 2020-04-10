from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20)
    lowerLimit = models.IntegerField()
    upperLimit = models.IntegerField()

    def __str__(self):
        return self.category
