from django.contrib import admin

admin.site.site_header = 'ENTREPRISES SOLUTIONS ADMIN'
admin.site.site_title = "Interface d'administration PRODUIT"

from produits.models import Produit
# Register your models here.
class ProduitAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'resume',
        'created',
    )

    list_filter = (
        'titre',
        'created',
        )

    search_fields = ['titre']

    list_per_page = 50

admin.site.register(Produit, ProduitAdmin)