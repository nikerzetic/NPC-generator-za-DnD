from django.db import models

from governing_body.models import GoverningBody
from character.models import Character


class Title(models.Model):
    name = models.CharField(max_length=100)
    concerning = models.ForeignKey(GoverningBody, blank=True, null=True, on_delete=models.SET_NULL)
    holders = models.ManyToManyField(Character)

    def __str__(self):
        return self.name
