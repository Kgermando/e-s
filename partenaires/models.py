from django.db import models

# Create your models here.
class Partenaire(models.Model):
    company = models.CharField(max_length=300)
    img_partenaire = models.ImageField(upload_to='partenaire_img/')
    created = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.company
