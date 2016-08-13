from __future__ import unicode_literals

#from django.db import models
from django.contrib.gis.db import models

# Create your models here.


#Datenfelder für Import CSV: Anrede (Herr, Frau, Keine Angabe), Vornamen (Textfeld),
# Nachname (Textfeld), E-Mail Adresse, PLZ (4-digit), Straße, Hausnummer

#Land, PLZ, Ort, Straße, Hausnummer, Türnummer, Anrede, Vorname, Nachname,
# E-Mail Adresse, Produktbedarf (Paket mit 500 Flyern)

class Activist(models.Model):
    anrede = models.CharField(max_length=100) #Anrede (Herr, Frau, Keine Angabe)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    postalcode = models.IntegerField() #PLZ (4-digit)
    municipal = models.CharField(max_length=500) #Ort
    street = models.CharField(max_length=500)
    house_number = models.CharField(max_length=100)
    coordinate = models.PointField()
    # todo:
    # - hash as link to user

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Meetup(models.Model):
    title = models.CharField(max_length=1000)
    datetime = models.DateTimeField()
    postalcode = models.IntegerField() #PLZ (4-digit)
    municipal = models.CharField(max_length=500) #Ort
    street = models.CharField(max_length=500)
    house_number = models.CharField(max_length=100)
    coordinate = models.PointField()
    activist = models.ManyToManyField(Activist)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
