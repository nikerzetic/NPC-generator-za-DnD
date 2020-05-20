from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


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

    strength = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(30)])    
    dexterity = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(30)])    
    constitution = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(30)])    
    intelligence = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(30)])    
    wisdom = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(30)])    
    charisma = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(30)])    

    appearance = models.ForeignKey(Appearance, blank=True, null=True, on_delete=models.SET_NULL)
    mannerism = models.ForeignKey(Mannerism, blank=True, null=True, on_delete=models.SET_NULL)
    interactionTrait = models.ForeignKey(InteractionTrait, blank=True, null=True, on_delete=models.SET_NULL)
    ideal = models.ForeignKey(Ideal, blank=True, null=True, on_delete=models.SET_NULL)
    bond = models.ForeignKey(Bond, blank=True, null=True, on_delete=models.SET_NULL)

    notes = models.TextField(max_length=1000, blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_absolute_url(self):
        return reverse('character:detail', kwargs={'pk': self.pk})
