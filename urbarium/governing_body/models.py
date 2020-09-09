from django.db import models
from django.urls import reverse


class Classification(models.Model):
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.description


class GoverningBody(models.Model):
    name = models.CharField(max_length=100)
    classification = models.ForeignKey(Classification, blank=True, null=True, on_delete=models.SET_NULL) # tip_organa
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('governing_body:detail', kwargs={'pk': self.pk})
