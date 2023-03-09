import datetime

from django.db import models
from django.utils import timezone


# Create your models here.


# Model house
class House(models.Model):
    name_house = models.CharField(max_length=2000)
    price_house = models.FloatField(10.000000)
    pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.name_house

    def was_published_recently_for_house_model(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Model Flat
class Flat(models.Model):
    name_flat = models.CharField(max_length=1999)
    price_flat = models.FloatField(5.000000)
    pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.name_flat

    def was_published_recently_for_flat_model(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Model Land
class Land(models.Model):
    name_land = models.CharField(max_length=1000)
    price_land = models.FloatField(1.000000)
    pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.name_land

    def was_published_recently_for_land_model(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Model NewConstruction
class NewConstruction(models.Model):
    name_new_construction = models.CharField(max_length=1998)
    price_new_construction = models.FloatField(5.000000)
    pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.name_new_construction

    def was_published_recently_for_new_construction_model(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Model Cities with relation one-to-many
class Cities(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    new_construction = models.ForeignKey(NewConstruction, on_delete=models.CASCADE)
    name_cities = models.CharField(max_length=2000)

    def __str__(self):
        return self.name_cities
