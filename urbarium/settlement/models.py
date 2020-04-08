from django.db import models

# Create your models here.


class AdministrativeUnit(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SettlementType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SettlementProperties(models.Model):
    sproperty = models.CharField(max_length=20)

    def __str__(self):
        return self.sproperty


class Settlement(models.Model):
    # Django avtomatsko doloci id, ki je primary key
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    administrative_unit = models.ForeignKey(AdministrativeUnit, blank=True, null=True, on_delete=models.SET_NULL)
    s_type = models.ForeignKey(SettlementType, blank=True, null=True, on_delete=models.SET_NULL)
    sproperty = models.ForeignKey(SettlementProperties, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
