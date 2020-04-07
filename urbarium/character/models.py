from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Appearance(models.Model):
    feature = models.CharField(max_length=100)
    def __str__(self):
        return self.feature

class Mannerism(models.Model):
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.description

class InteractionTrait(models.Model):
    trait = models.CharField(max_length=20)
    def __str__(self):
        return self.description

class Ideal(models.Model):
    description = models.CharField(max_length=20)
    def __str__(self):
        return self.description

class Bond(models.Model):
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.description


class Character(models.Model):
    # Django avtomatsko doloci id, ki je primary key
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True)
    gender = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.SET_NULL)
    race = models.ForeignKey(Race, blank=True, null=True, on_delete=models.SET_NULL)
    age = models.IntegerField()

    class Abilities(models.TextChoices):
        STRENGTH = 'STR'
        DEXTERITY = 'DEX'
        CONSTITUTION = 'CON'
        INTELIGENCE = 'INT'
        WISDOM = 'WIS'
        CHARISMA = 'CHA'

    high_ability = models.CharField(max_length=3, choices=Abilities.choices, default=Abilities.STRENGTH)
    low_ability = models.CharField(
        max_length=3, choices=Abilities.choices,
        default=Abilities.INTELIGENCE
        )        

    appearance = models.ForeignKey(Appearance, blank=True, null=True, on_delete=models.SET_NULL)
    mannerism = models.ForeignKey(Mannerism, blank=True, null=True, on_delete=models.SET_NULL)
    interactionTrait = models.ForeignKey(InteractionTrait, blank=True, null=True, on_delete=models.SET_NULL)
    ideal = models.ForeignKey(Ideal, blank=True, null=True, on_delete=models.SET_NULL)
    bond = models.ForeignKey(Bond, blank=True, null=True, on_delete=models.SET_NULL)

    notes = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname
