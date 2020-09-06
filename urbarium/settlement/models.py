from django.db import models
from django.urls import reverse


class SettlementType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Location(models.Model):
    locationName = models.CharField(max_length=20)

    def __str__(self):
        return self.locationName


class KnownFor(models.Model):
    characteristic = models.CharField(max_length=20)

    def __str__(self):
        return self.characteristic


class Economy(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Settlement(models.Model):
    # Django avtomatsko doloci id, ki je primary key

    name = models.CharField(max_length=50)
    category = models.ForeignKey(SettlementType, blank=True, null=True, on_delete=models.SET_NULL)
    population = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    economy = models.ForeignKey(Economy, blank=True, null=True, on_delete=models.SET_NULL)
    knownfor = models.ForeignKey(KnownFor, blank=True, null=True, on_delete=models.SET_NULL)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('settlement:detail', kwargs={'pk': self.pk})
