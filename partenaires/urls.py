from django.urls import path

from partenaires.views import partenaires_view, partenaire_detail

app_name = 'partenaires'

urlpatterns = [
    path('', partenaires_view, name='partenaires'),
    path('partenaire_detail/<slug:slug>/', partenaire_detail, name='partenaire_detail'),
]
