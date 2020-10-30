from django.urls import path

from produits.views import produits_view

app_name = 'produits'

urlpatterns = [
    path('', produits_view, name='produits'),
]
