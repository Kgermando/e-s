from django.contrib import admin

from documentations.models import Documentation

admin.site.site_header = 'ENTREPRISES SOLUTIONS ADMIN'
admin.site.site_title = "Interface d'administration documentations"
# Register your models here.

class DocumentationsAdmin(admin.ModelAdmin):
    list_display = (
        'categorie',
        'question',
    )

    list_filter = (
        'categorie',
        'question',
        )

    search_fields = ['categorie', 'question',]

    list_per_page = 50

admin.site.register(Documentation, DocumentationsAdmin)
