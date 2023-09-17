from django.db import models
# Create your models here.

class Devi(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    type_appart = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(max_length=1500, null=True, blank=True)
    def __str__(self):
        return self.nom

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100)
    note = models.TextField(max_length=1500)
    def __str__(self):
        return self.nom
class Bloc(models.Model):
    letter = models.CharField(max_length=1, primary_key=True)
    etat = models.TextField(max_length=1500, default="Travaux pas entamés")
    def __str__(self):
        return self.letter

class Image(models.Model):
    image = models.ImageField(upload_to='images')
