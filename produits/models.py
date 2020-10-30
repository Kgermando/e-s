from django.db import models

# Create your models here.
class Produit(models.Model):
    title_produit = models.CharField(max_length=300)