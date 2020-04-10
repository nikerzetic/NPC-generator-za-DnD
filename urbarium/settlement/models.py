from django.db import models


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
    economyTpye = models.CharField(max_length=20)

    def __str__(self):
        return self.economyType


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
