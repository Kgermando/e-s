from django.contrib import admin

admin.site.site_header = 'ENTREPRISES SOLUTIONS ADMIN'
admin.site.site_title = "Interface d'administration Dashboard"

from partenaires.models import Partenaire
# Register your models here.
class PartenaireAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'created',
    )

    list_filter = (
        'company',
        'created',
        )

    search_fields = ['company']

    list_per_page = 50

admin.site.register(Partenaire, PartenaireAdmin)