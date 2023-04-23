from django.db import models

class Classe(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image_representative = models.ImageField(upload_to='classes_representatives/', blank=True, null=True)

class Image(models.Model):
    image = models.ImageField(upload_to='raw/')
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)
