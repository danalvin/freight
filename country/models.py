from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class City(models.Model):
    Country = models.ForeignKey(Country, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    rate = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"
