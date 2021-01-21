from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import widgets

from dashboard.models import (Forms_Entreprise)


# class DownloadFileWidget(widgets.AdminFileWidget):
#     id = None
#     template_name = 'widgets/download_file_input.html'

#     def __init__(self, id, attrs=None):
#         self.id = id
#         super().__init__(attrs)

#     def get_context(self, name, value, attrs):
#         context = super().get_context(name, value, attrs)
#         print(self, name, value, attrs, self.id)
#         context['download_url'] = reverse('attachment', kwargs={'pk': self.id})
#         return context


# class FormsEntrepriseAdmin(admin.ModelAdmin):
#     list_display = ['id', 'company', 'logo']
#     search_fields = ('company',)
#     my_id_for_formfield = None

#     def get_form(self, request, obj=None, **kwargs):
#         if obj:
#             self.my_id_for_formfield = obj.id
#         return super(FormsEntrepriseAdmin, self).get_form(request, obj=obj, **kwargs)

#     def formfield_for_dbfield(self, db_field, **kwargs):
#         if self.my_id_for_formfield:
#             if db_field.name == 'file':
#                 kwargs['widget'] = DownloadFileWidget(
#                     id=self.my_id_for_formfield)

#         return super(FormsEntrepriseAdmin, self).formfield_for_dbfield(db_field, **kwargs)

#     def _get_download_url(self, instance):
#         return format_html('<a href="{}">{}</a>', reverse('attachment', kwargs={'pk': instance.id}), instance.filename)

#     _get_download_url.short_description = 'download'


admin.site.register(Forms_Entreprise, FormsEntrepriseAdmin)
