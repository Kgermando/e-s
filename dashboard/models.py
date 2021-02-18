from django.db import models
from tinymce import HTMLField
from django.db.models.signals import pre_save
from es.utils import (
    unique_slug_generator_dashboard_Opportunite,
    unique_slug_generator_dashboard_Annonce,
    unique_slug_generator_dashboard_Fidelite,
    unique_slug_generator_dashboard_Marketing,
    unique_slug_generator_dashboard_Commerciale
)



# Create your models here.
class Forms_Entreprise(models.Model):
    company = models.CharField(max_length=300)
    secteur = models.CharField(max_length=300)
    description = HTMLField('description')
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    telephone_2 = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='entreprise_img/', blank=True)
    rccm = models.CharField(max_length=300)
    id_nat = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    adresse = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company

class Forms_Artisans(models.Model):
    company = models.CharField(max_length=300)
    secteur = models.CharField(max_length=300)
    description = HTMLField('description')
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    telephone_2 = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='artisans_img/', blank=True)
    date = models.CharField(max_length=300)
    adresse = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company


class Forms_Consultant(models.Model):
    company = models.CharField(max_length=300)
    secteur = models.CharField(max_length=300)
    specialite = models.CharField(max_length=300)
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    telephone_2 = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='consulant_img/')
    date = models.CharField(max_length=300)
    adresse = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company


class Forms_Partenaire(models.Model):
    company = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    secteur = models.CharField(max_length=300)
    description = HTMLField('description')
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    telephone_2 = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='partenaire_img/')
    adresse = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company


class Forms_Investisseur(models.Model):
    company = models.CharField(max_length=300)
    motivation = models.CharField(max_length=300)
    secteur = models.CharField(max_length=300)
    description = HTMLField('description')
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    telephone_2 = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='investisseur_img/')
    adresse = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company


class Opportunite(models.Model):
    titre = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    description = HTMLField('description')
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    img = models.ImageField(upload_to='opportunite_img/')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("dashboard:opportunites-detail", kwargs={"id": self.id})


class Annonce(models.Model):
    titre = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    description = HTMLField('description')
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    img = models.ImageField(upload_to='annonce_img/')
    created = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("dashboard:annonces-detail", kwargs={"id": self.id})

class Fidelite(models.Model):
    titre = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    description = HTMLField('description')
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    img = models.ImageField(upload_to='fidelite_img/')
    created = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("dashboard:fidelites-detail", kwargs={"id": self.id})


class Marketing(models.Model):
    titre = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    description = HTMLField('description')
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    img = models.ImageField(upload_to='marketing_img/')
    created = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("dashboard:marketing-detail", kwargs={"id": self.id})


class Commerciale(models.Model):
    titre = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    description = HTMLField('description')
    url =  models.URLField(null=True, blank=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=300)
    img = models.ImageField(upload_to='commerciale/')
    created = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("dashboard:commerciale-detail", kwargs={"id": self.id})




def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_dashboard_Opportunite(instance)

pre_save.connect(tag_pre_save_receiver, sender=Opportunite)

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_dashboard_Annonce(instance)

pre_save.connect(tag_pre_save_receiver, sender=Annonce) 

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_dashboard_Fidelite(instance)

pre_save.connect(tag_pre_save_receiver, sender=Fidelite)

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_dashboard_Marketing(instance)

pre_save.connect(tag_pre_save_receiver, sender=Marketing)

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_dashboard_Commerciale(instance)

pre_save.connect(tag_pre_save_receiver, sender=Commerciale)