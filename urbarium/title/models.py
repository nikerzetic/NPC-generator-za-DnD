from django.db import models

from governing_body.models import GoverningBody
from character.models import Character
from django.urls import reverse


class Title(models.Model):
    name = models.CharField(max_length=100)
    concerning = models.ForeignKey(GoverningBody, blank=True, null=True, on_delete=models.SET_NULL)
    holders = models.ManyToManyField(Character)
    current_holder = models.ForeignKey(Character, blank=True, null=True, on_delete=models.SET_NULL, related_name='current_holder')
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('title:detail', kwargs={'pk': self.pk})
