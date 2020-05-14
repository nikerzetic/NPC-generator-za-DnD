from django.db import models
from django.urls import reverse


class SettlementType(models.Model):
    name = models.CharField(max_length=20)
    lowerLimit = models.IntegerField()
    upperLimit = models.IntegerField()

    def difference(self):
        return self.upperLimit - self.lowerLimit

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
    population = models.IntegerField()
    category = models.ForeignKey(SettlementType, blank=True, null=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    know_for = models.ForeignKey(KnownFor, blank=True, null=True, on_delete=models.SET_NULL)
    economy = models.ForeignKey(Economy, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('settlement:edit', kwargs={'pk': self.pk})
