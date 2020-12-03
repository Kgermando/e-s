from django.contrib import admin

admin.site.site_header = 'ENTREPRISES SOLUTIONS ADMIN'
admin.site.site_title = "Interface d'administration APP"


from app.models import ContactForm, Team
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'objet_name',
        'email_id',
        'phone_num',
        'created',
    )

    list_filter = (
        'first_name',
        'last_name',
        'objet_name',
        'email_id',
        'phone_num',
        'created',
        )

    search_fields = ['first_name',
                    'last_name',
                    'objet_name',
                    'email_id',
                    'phone_num']

    list_per_page = 50

admin.site.register(ContactForm, ContactAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'img_profile',
        'prenom_nom',
        'grade',
        'created',
    )

    list_filter = (
        'prenom_nom',
        'grade',
        'created',
        )

    search_fields = ['prenom_nom', 'grade']

    list_per_page = 50

admin.site.register(Team, TeamAdmin)

# class NewsletterAdmin(admin.ModelAdmin):
#     list_display = (
#         'email',
#         'created',
#     )

#     list_filter = (
#         'created',
#         )

#     search_fields = ['email', 'created']

#     list_per_page = 50

# admin.site.register(Newsletter, NewsletterAdmin)