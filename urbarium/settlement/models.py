from django.db import models


class SettlementType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SettlementCharacteristic1(models.Model):
    characteristic = models.CharField(max_length=20)

    def __str__(self):
        return self.characteristic


class SettlementCharacteristic2(models.Model):
    characteristic = models.CharField(max_length=20)

    def __str__(self):
        return self.characteristic


class SettlementCharacteristic3(models.Model):
    characteristic = models.CharField(max_length=20)

    def __str__(self):
        return self.characteristic


class Settlement(models.Model):
    # Django avtomatsko doloci id, ki je primary key
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    category = models.ForeignKey(SettlementType, blank=True, null=True, on_delete=models.SET_NULL)
    characteristic1 = models.ForeignKey(SettlementCharacteristic1, blank=True, null=True, on_delete=models.SET_NULL)
    characteristic2 = models.ForeignKey(SettlementCharacteristic2, blank=True, null=True, on_delete=models.SET_NULL)
    characteristic3 = models.ForeignKey(SettlementCharacteristic3, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
