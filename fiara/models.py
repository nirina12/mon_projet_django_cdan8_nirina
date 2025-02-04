from django.db import models

class Personne(models.Model):
    OPTIONS = (
        ('masculin', 'masculin'),
        ('feminin', 'feminin'),
    )
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255,null=False)
    prenom = models.CharField(max_length=255,null=False)
    age = models.IntegerField(null=False)
    genre = models.CharField(max_length=20, choices=OPTIONS)

class Voiture(models.Model):
    immatriculation = models.CharField(max_length=8, primary_key=True)
    marque = models.CharField(max_length=255,null=False)
    proprietaire = models.ForeignKey(Personne, on_delete=models.CASCADE, null=False)
    image = models.CharField(max_length=255,null=False)
