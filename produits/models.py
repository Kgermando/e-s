from django.db import models
from django.db.models.signals import pre_save
from es.utils import unique_slug_generator_produit

# Create your models here.
class Produit(models.Model):
    titre = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    resume = models.TextField(max_length=300)
    description = models.TextField()
    img = models.ImageField(upload_to='produit_img/')
    created = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("produits:product_detail", kwargs={"slug": self.slug})


# class Innovation(models.Model):
#     titre = models.CharField(max_length=300)
#     slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
#     secteur = models.CharField(max_length=300)
#     description = models.TextField()
#     img = models.ImageField(upload_to='innovation_img/')
#     created = models.DateTimeField(auto_now=False)

#     def __str__(self):
#         return self.titre

    # def get_absolute_url(self):
    #     return reverse("docs:doc_detail", kwargs={"slug": self.slug})


# class Formation(models.Model):
#     titre = models.CharField(max_length=300)
#     slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
#     secteur = models.CharField(max_length=300)
#     description = models.TextField()
#     img = models.ImageField(upload_to='formation_img/')
#     created = models.DateTimeField(auto_now=False)

#     def __str__(self):
#         return self.titre

#     # def get_absolute_url(self):
#     #     return reverse("docs:doc_detail", kwargs={"slug": self.slug})


# class Accompagnement(models.Model):
#     titre = models.CharField(max_length=300)
#     slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
#     secteur = models.CharField(max_length=300)
#     description = models.TextField()
#     img = models.ImageField(upload_to='accompagenement_img/')
#     created = models.DateTimeField(auto_now=False)

#     def __str__(self):
#         return self.titre

#     # def get_absolute_url(self):
#     #     return reverse("docs:doc_detail", kwargs={"slug": self.slug})


# class Consultant(models.Model):
#     titre = models.CharField(max_length=300)
#     slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
#     secteur = models.CharField(max_length=300)
#     description = models.TextField()
#     img = models.ImageField(upload_to='consultant_img/')
#     created = models.DateTimeField(auto_now=False)

#     def __str__(self):
#         return self.titre

#     # def get_absolute_url(self):
#     #     return reverse("docs:doc_detail", kwargs={"slug": self.slug})


# class Marketing(models.Model):
#     titre = models.CharField(max_length=300)
#     slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
#     secteur = models.CharField(max_length=300)
#     description = models.TextField()
#     img = models.ImageField(upload_to='marketing_img/')
#     created = models.DateTimeField(auto_now=False)

#     def __str__(self):
#         return self.titre

#     # def get_absolute_url(self):
#     #     return reverse("docs:doc_detail", kwargs={"slug": self.slug})


# class Communication(models.Model):
#     titre = models.CharField(max_length=300)
#     slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
#     secteur = models.CharField(max_length=300)
#     description = models.TextField()
#     img = models.ImageField(upload_to='communication_img/')
#     created = models.DateTimeField(auto_now=False)

#     def __str__(self):
#         return self.titre

#     # def get_absolute_url(self):
#     #     return reverse("docs:doc_detail", kwargs={"slug": self.slug})


# class Immobilie(models.Model):
#     titre = models.CharField(max_length=300)
#     slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
#     secteur = models.CharField(max_length=300)
#     description = models.TextField()
#     img = models.ImageField(upload_to='immobilie_img/')
#     created = models.DateTimeField(auto_now=False)

#     def __str__(self):
#         return self.titre

#     # def get_absolute_url(self):
#     #     return reverse("docs:doc_detail", kwargs={"slug": self.slug})


# class Transport(models.Model):
#     titre = models.CharField(max_length=300)
#     slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
#     secteur = models.CharField(max_length=300)
#     description = models.TextField()
#     img = models.ImageField(upload_to='transport_img/')
#     created = models.DateTimeField(auto_now=False)

#     def __str__(self):
#         return self.titre

#     # def get_absolute_url(self):
#     #     return reverse("docs:doc_detail", kwargs={"slug": self.slug})


# class Assurance_et_finance(models.Model):
#     titre = models.CharField(max_length=300)
#     slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
#     secteur = models.CharField(max_length=300)
#     description = models.TextField()
#     img = models.ImageField(upload_to='assurance_img/')
#     created = models.DateTimeField(auto_now=False)

#     def __str__(self):
#         return self.titre

#     # def get_absolute_url(self):
#     #     return reverse("docs:doc_detail", kwargs={"slug": self.slug})




def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_produit(instance)

pre_save.connect(tag_pre_save_receiver, sender=Produit)