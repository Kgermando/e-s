
from django.urls import path

from dashboard.views import dashboard_view, dashboard_forms_entreprise, \
    dashboard_forms_artisans, dashboard_forms_consultant, dashboard_forms_partenaire, \
    dashboard_forms_investisseurs, dashboard_opportunites, dashboard_annonces, \
    dashboard_fidelites, dashboard_marketing, dashboard_commerciale


app_name = 'dashboard'

urlpatterns = [
    path('dashboard', dashboard_view, name='dashboard'),
    path('forms_entreprise', dashboard_forms_entreprise, name='forms_entreprise'),
    path('forms_artisans', dashboard_forms_artisans, name='forms_artisans'),
    path('forms_consultant', dashboard_forms_consultant, name='forms_consultant'),
    path('forms_partenaire', dashboard_forms_partenaire, name='forms_partenaire'),
    path('forms_inestisseurs', dashboard_forms_investisseurs, name='forms_inestisseurs'),
    path('opportunites', dashboard_opportunites, name='opportunites'),
    path('annonces', dashboard_annonces, name='annonces'),
    path('fidelites', dashboard_fidelites, name='fidelites'),
    path('marketing', dashboard_marketing, name='marketing'),
    path('commerciale', dashboard_commerciale, name='commerciale'),
]
