from django.contrib import admin

admin.site.site_header = 'ENTREPRISES SOLUTIONS ADMIN'
admin.site.site_title = "Interface d'administration Solutions"

from solutions.models import Entreprise_solution, Artisans_solution, Consultance_solution
# Register your models here.

class Entreprise_solutionAdmin(admin.ModelAdmin):
    list_display = (
        'logo_entreprise',
        'nom',
        'secteur_entreprise',
        'fonctions_entreprise',
        'telephone_entreprise',
        'email_entreprise',
    )

    list_filter = (
        'nom',
        'secteur_entreprise',
        'fonctions_entreprise',
        )

    search_fields = ['nom', 'secteur_entreprise', 'fonctions_entreprise']

    list_per_page = 50

admin.site.register(Entreprise_solution, Entreprise_solutionAdmin)


class Artisans_solutionAdmin(admin.ModelAdmin):
    list_display = (
        'logo_artisans',
        'nom',
        'secteur_artisans',
        'fonctions_artisans',
        'telephone_artisans',
        'email_artisans',
    )

    list_filter = (
        'nom',
        'secteur_artisans',
        'fonctions_artisans',
        )

    search_fields = ['nom', 'secteur_artisans', 'fonctions_artisans']

    list_per_page = 50

admin.site.register(Artisans_solution, Artisans_solutionAdmin)


class Consultance_solutionAdmin(admin.ModelAdmin):
    list_display = (
        'logo_consultance',
        'nom',
        'secteur_consultance',
        'fonctions_consultance',
        'telephone_consultance',
        'email_consultance',
    )

    list_filter = (
        'nom',
        'secteur_consultance',
        'fonctions_consultance',
        )

    search_fields = ['nom', 'secteur_consultance', 'fonctions_consultance']

    list_per_page = 50

admin.site.register(Consultance_solution, Consultance_solutionAdmin)
