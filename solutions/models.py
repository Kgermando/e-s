from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from es.utils import unique_slug_generator_solution
from es.constant import SECTEUR_ENTREPRISES

from tinymce import HTMLField

# Create your models here.
class Entreprise_solution(models.Model):
    """
    Entreprise model
    """
    nom = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    secteur_entreprise = models.CharField(max_length=300, choices=SECTEUR_ENTREPRISES)
    fonctions_entreprise = models.CharField(max_length=500)
    logo_entreprise = models.ImageField(upload_to= 'entreprise_solution_img/')
    telephone_entreprise = models.DecimalField(max_digits=13, decimal_places=0) 
    telephone_2_entreprise = models.DecimalField(max_digits=13, decimal_places=0) 
    email_entreprise = models.EmailField()
    site_web = models.URLField(blank=True)
    description_entreprise = HTMLField('description_entreprise')
    competence_entreprise = models.CharField(max_length=500)
    sociauFB_entreprise = models.URLField(blank=True, help_text='Copiez le lien de compte Facebook et collez le ici')
    sociauTW_entreprise = models.URLField(blank=True, help_text='Copiez le lien de compte Twitter et collez le ici')
    sociauINS_entreprise = models.URLField(blank=True, help_text='Copiez le lien de compte Instagram et collez le ici')
    sociauIN_entreprise = models.URLField(blank=True, help_text='Copiez le lien de compte LinkedIN et collez le ici')
    page_vues = models.IntegerField(default=0, verbose_name="Nombre des vues")

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("solutions:entreprise_solutions_detail", kwargs={"id": self.id})


class Artisans_solution(models.Model):
    """
    Artisans model
    """
    nom = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    secteur_artisans = models.CharField(max_length=300, choices=SECTEUR_ENTREPRISES)
    fonctions_artisans = models.CharField(max_length=500)
    logo_artisans = models.ImageField(upload_to= 'entreprise_solution_img/')
    telephone_artisans = models.DecimalField(max_digits=13, decimal_places=0) 
    telephone_2_artisans = models.DecimalField(max_digits=13, decimal_places=0) 
    email_artisans = models.EmailField()
    site_web = models.URLField(blank=True)
    description_artisans = HTMLField('description_artisans')
    competence_artisans = models.CharField(max_length=500)
    sociauFB_artisans = models.URLField(blank=True, help_text='Copiez le lien de compte Facebook et collez le ici')
    sociauTW_artisans = models.URLField(blank=True, help_text='Copiez le lien de compte Twitter et collez le ici')
    sociauINS_artisans = models.URLField(blank=True, help_text='Copiez le lien de compte Instagram et collez le ici')
    sociauIN_artisans = models.URLField(blank=True, help_text='Copiez le lien de compte LinkedIN et collez le ici')
    page_vues = models.IntegerField(default=0, verbose_name="Nombre des vues")

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("solutions:artisans_solution_detail", kwargs={"id": self.id})


 
class Consultance_solution(models.Model):
    """
    Consultance model
    """
    nom = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    secteur_consultance = models.CharField(max_length=300, choices=SECTEUR_ENTREPRISES)
    fonctions_consultance = models.CharField(max_length=500)
    logo_consultance = models.ImageField(upload_to= 'entreprise_solution_img/')
    telephone_consultance = models.DecimalField(max_digits=13, decimal_places=0) 
    telephone_2_consultance = models.DecimalField(max_digits=13, decimal_places=0) 
    email_consultance = models.EmailField()
    site_web = models.URLField(blank=True)
    description_consultance = HTMLField('description_consultance')
    competence_consultance = models.CharField(max_length=500)
    sociauFB_consultance = models.URLField(blank=True, help_text='Copiez le lien de compte Facebook et collez le ici')
    sociauTW_consultance = models.URLField(blank=True, help_text='Copiez le lien de compte Twitter et collez le ici')
    sociauINS_consultance = models.URLField(blank=True, help_text='Copiez le lien de compte Instagram et collez le ici')
    sociauIN_consultance = models.URLField(blank=True, help_text='Copiez le lien de compte LinkedIN et collez le ici')
    page_vues = models.IntegerField(default=0, verbose_name="Nombre des vues")

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("solutions:consultance_solutions_detail", kwargs={"id": self.id})


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_solution(instance)

pre_save.connect(tag_pre_save_receiver, sender=Entreprise_solution)
pre_save.connect(tag_pre_save_receiver, sender=Artisans_solution)
pre_save.connect(tag_pre_save_receiver, sender=Consultance_solution)
