from django.db import models
from django.db.models.signals import pre_save
from es.utils import unique_slug_generator_partenaire

# Create your models here.
class Partenaire(models.Model):
    company = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    img_partenaire = models.ImageField(upload_to='partenaire_img/')
    created = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("partenaires:partenaire_detail", kwargs={"slug": self.slug})


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_produit(instance)

pre_save.connect(tag_pre_save_receiver, sender=Partenaire)