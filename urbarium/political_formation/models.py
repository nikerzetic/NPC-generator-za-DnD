from django.db import models

from governing_body.models import GoverningBody


class Classification(models.Model):
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.description

class Government(models.Model):
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.description

class PoliticalFormation(models.Model):
    name = models.CharField(max_length=100)
    classification = models.ForeignKey(Classification, blank=True, null=True, on_delete=models.SET_NULL)
    government = models.ForeignKey(Government, blank=True, null=True, on_delete=models.SET_NULL)
    governing_body = models.ForeignKey(GoverningBody, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
