from django.db import models

# Create your models here.
class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    objet_name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=101)
    phone_num = models.CharField(max_length=15)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Message de ' + self.first_name + ' ' + self.last_name


class Team(models.Model):
    prenom_nom = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    img_profile = models.ImageField(upload_to='team_img/')
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.prenom_nom

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("app:about_detail", kwargs={"id": self.id}) 

# class Newsletter(models.Model):
#     email = models.EmailField()
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.email