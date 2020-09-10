from django.db import models
from django.urls import reverse

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
    classification = models.ForeignKey(Classification, blank=True, null=True, on_delete=models.SET_NULL) # tip_tvorbe
    government = models.ForeignKey(Government, blank=True, null=True, on_delete=models.SET_NULL) # tip_oblasti
    governing_body = models.ForeignKey(GoverningBody, blank=True, null=True, on_delete=models.SET_NULL) # organ
    public = models.BooleanField(default=False)
    part_of = models.ForeignKey('self',  blank=True, null=True, on_delete=models.SET_NULL, related_name='%(class)s_inclusion')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('political_formation:detail', kwargs={'pk': self.pk})
