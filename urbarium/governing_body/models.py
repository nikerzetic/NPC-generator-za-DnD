from django.db import models


class Classification(models.Model):
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.description


class GoverningBody(models.Model):
    name = models.CharField(max_length=100)
    classification = models.ForeignKey(Classification, blank=True, null=True, on_delete=models.SET_NULL) # tip_organa

    def __str__(self):
        return self.name
