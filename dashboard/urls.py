
from django.urls import path

from dashboard.views import dashboard_stats, dashboard_forms_entreprise, \
    dashboard_forms_artisans, dashboard_forms_consultant, dashboard_forms_partenaire, \
    dashboard_forms_investisseurs, dashboard_opportunites, dashboard_annonces, \
    dashboard_fidelites, dashboard_marketing, dashboard_commerciale, opportunite_detail, annonce_detail, \
    fidelites_detail, marketing_detail, commerciale_detail


app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_stats, name='dashboard'),
    path('forms_entreprise/', dashboard_forms_entreprise, name='forms_entreprise'),
    path('forms_artisans/', dashboard_forms_artisans, name='forms_artisans'),
    path('forms_consultant/', dashboard_forms_consultant, name='forms_consultant'),
    path('forms_partenaire/', dashboard_forms_partenaire, name='forms_partenaire'),
    path('forms_inestisseurs/', dashboard_forms_investisseurs, name='forms_inestisseurs'),
    path('opportunites/', dashboard_opportunites, name='opportunites'),
    path('opportunites/<int:id>', opportunite_detail, name='opportunites-detail'),
    path('annonces/', dashboard_annonces, name='annonces'),
    path('annonces/<int:id>', annonce_detail, name='annonces-detail'),
    path('fidelites/', dashboard_fidelites, name='fidelites'),
    path('fidelites/<int:id>', fidelites_detail, name='fidelites-detail'),
    path('marketing/', dashboard_marketing, name='marketing'),
    path('marketing/<int:id>', marketing_detail, name='marketing-detail'),
    path('commerciale/', dashboard_commerciale, name='commerciale'),
    path('commerciale/<int:id>', commerciale_detail, name='commerciale-detail'),
]
