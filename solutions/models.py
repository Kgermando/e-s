from django.db import models
from django.db.models.signals import pre_save
from es.utils import unique_slug_generator_solution
from es.constant import SECTEUR_ENTREPRISES
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
    description_entreprise = models.CharField(max_length=500)
    competence_entreprise = models.CharField(max_length=500)
    sociauFB_entreprise = models.URLField(blank=True, help_text='Copiez le lien de compte Facebook et collez le ici')
    sociauTW_entreprise = models.URLField(blank=True, help_text='Copiez le lien de compte Twitter et collez le ici')
    sociauINS_entreprise = models.URLField(blank=True, help_text='Copiez le lien de compte Instagram et collez le ici')
    sociauIN_entreprise = models.URLField(blank=True, help_text='Copiez le lien de compte LinkedIN et collez le ici')

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("solutions:entreprise_solutions_detail", kwargs={"slug": self.slug})


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
    description_artisans = models.CharField(max_length=500)
    competence_artisans = models.CharField(max_length=500)
    sociauFB_artisans = models.URLField(blank=True, help_text='Copiez le lien de compte Facebook et collez le ici')
    sociauTW_artisans = models.URLField(blank=True, help_text='Copiez le lien de compte Twitter et collez le ici')
    sociauINS_artisans = models.URLField(blank=True, help_text='Copiez le lien de compte Instagram et collez le ici')
    sociauIN_artisans = models.URLField(blank=True, help_text='Copiez le lien de compte LinkedIN et collez le ici')

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("solutions:entreprise_solutions_detail", kwargs={"slug": self.slug})



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
    description_consultance = models.CharField(max_length=500)
    competence_consultance = models.CharField(max_length=500)
    sociauFB_consultance = models.URLField(blank=True, help_text='Copiez le lien de compte Facebook et collez le ici')
    sociauTW_consultance = models.URLField(blank=True, help_text='Copiez le lien de compte Twitter et collez le ici')
    sociauINS_consultance = models.URLField(blank=True, help_text='Copiez le lien de compte Instagram et collez le ici')
    sociauIN_consultance = models.URLField(blank=True, help_text='Copiez le lien de compte LinkedIN et collez le ici')

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("solutions:entreprise_solutions_detail", kwargs={"slug": self.slug})


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Entreprise_solution)