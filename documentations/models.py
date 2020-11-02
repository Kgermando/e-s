from django.db import models
from django.db.models.signals import pre_save
from es.utils import unique_slug_generator

from es.constant import CATEGORIES
# Create your models here.
class Documentation(models.Model):
    img_docs = models.ImageField(upload_to='docs_img/')
    categorie =  models.CharField(max_length=300, choices=CATEGORIES)
    question = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    reponse = models.TextField()

    def __str__(self):
        return self.question


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("docs:doc_detail", kwargs={"slug": self.slug})


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Documentation)
