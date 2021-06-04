from django.db import models
from django.db.models.base import Model


# Les départements
class Depart(models.Model):
    intitule = models.CharField(max_length=150)
    etage = models.IntegerField()


# Les employes
class Employe(models.Model):
    depart = models.ForeignKey(to=Depart, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    age = models.IntegerField()
    ville = models.CharField(max_length=200)
    poste = models.CharField(max_length=200)
    salaire = models.FloatField(max_length=100000)



