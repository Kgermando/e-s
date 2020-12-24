from django.contrib import admin

admin.site.site_header = 'ENTREPRISES SOLUTIONS ADMIN'
admin.site.site_title = "Interface d'administration Dashboard"

from dashboard.models import Forms_Entreprise, Forms_Artisans, Forms_Consultant, Forms_Partenaire, \
    Forms_Investisseur, Opportunite, Annonce, Fidelite, Marketing, Commerciale
# Register your models here.
class Forms_EntrepriseAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'secteur',
        'email',
        'telephone',
        'rccm',
        'id_nat',
        'created',
    )

    list_filter = (
        'company',
        'secteur',
        'email',
        'telephone',
        'rccm',
        'id_nat',
        'created',
        )

    search_fields = ['company',
        'secteur',
        'email',
        'telephone',
        'rccm',
        'id_nat',]

    list_per_page = 50

admin.site.register(Forms_Entreprise, Forms_EntrepriseAdmin)


class Forms_ConsultantAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'secteur',
        'email',
        'telephone',
        'created',
    )

    list_filter = (
        'company',
        'secteur',
        'email',
        'telephone',
        'created',
        )

    search_fields = ['company',
        'secteur',
        'email',
        'telephone',]

    list_per_page = 50

admin.site.register(Forms_Consultant, Forms_ConsultantAdmin)

class Forms_ArtisansAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'secteur',
        'email',
        'telephone',
        'created',
    )

    list_filter = (
        'company',
        'secteur',
        'email',
        'telephone',
        'created',
        )

    search_fields = ['company',
        'secteur',
        'email',
        'telephone',]

    list_per_page = 50

admin.site.register(Forms_Artisans, Forms_ArtisansAdmin)


class Forms_PartenaireAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'secteur',
        'type',
        'email',
        'telephone',
        'created',
    )

    list_filter = (
        'company',
        'secteur',
        'type',
        'email',
        'telephone',
        'created',
        )

    search_fields = ['company',
        'secteur',
        'type',
        'email',
        'telephone',]

    list_per_page = 50

admin.site.register(Forms_Partenaire, Forms_PartenaireAdmin)


class Forms_InvestisseurAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'secteur',
        'motivation',
        'email',
        'telephone',
        'created',
    )

    list_filter = (
        'company',
        'secteur',
        'motivation',
        'email',
        'telephone',
        'created',
        )

    search_fields = ['company',
        'secteur',
        'motivation',
        'email',
        'telephone',]

    list_per_page = 50

admin.site.register(Forms_Investisseur, Forms_InvestisseurAdmin)


class OpportuniteAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
    )

    list_filter = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
        )

    search_fields = ['titre',
        'secteur',
        'email',
        'telephone',]

    list_per_page = 50

admin.site.register(Opportunite, OpportuniteAdmin)


class AnnonceAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
    )

    list_filter = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
        )

    search_fields = ['titre',
        'secteur',
        'email',
        'telephone',]

    list_per_page = 50

admin.site.register(Annonce, AnnonceAdmin)


class FideliteAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
    )

    list_filter = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
        )

    search_fields = ['titre',
        'secteur',
        'email',
        'telephone',]

    list_per_page = 50

admin.site.register(Fidelite, FideliteAdmin)


class MarketingAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
    )

    list_filter = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
        )

    search_fields = ['titre',
        'secteur',
        'email',
        'telephone',]

    list_per_page = 50

admin.site.register(Marketing, MarketingAdmin)


class CommercialeAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
    )

    list_filter = (
        'titre',
        'secteur',
        'email',
        'telephone',
        'created',
        )

    search_fields = ['titre',
        'secteur',
        'email',
        'telephone',]

    list_per_page = 50

admin.site.register(Commerciale, CommercialeAdmin)

