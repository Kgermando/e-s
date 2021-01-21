from django.urls import path

from administration.views import forms_download

app_name = 'administration'

urlpatterns = [
    path('', forms_download, name='forms_download'),
]
