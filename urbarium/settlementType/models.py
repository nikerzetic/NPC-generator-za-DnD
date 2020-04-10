from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20)
    lowerLimit = models.IntegerField()
    upperLimit = models.IntegerField()

    def difference(self):
        return self.upperLimit - self.lowerLimit

    def __str__(self):
        return self.category
