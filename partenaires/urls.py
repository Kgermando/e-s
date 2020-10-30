from django.urls import path

from partenaires.views import partenaires_view

app_name = 'partenaires'

urlpatterns = [
    path('', partenaires_view, name='partenaires'),
]
