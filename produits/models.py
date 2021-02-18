from django.db import models
from django.db.models.signals import pre_save
from es.utils import unique_slug_generator_produit

from tinymce import HTMLField

# Create your models here.
class Produit(models.Model):
    titre = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    resume = models.TextField(max_length=300)
    description = HTMLField('description')
    img = models.ImageField(upload_to='produit_img/')
    created = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("produits:product_detail_id", kwargs={"id": self.id})


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_produit(instance)

pre_save.connect(tag_pre_save_receiver, sender=Produit)

