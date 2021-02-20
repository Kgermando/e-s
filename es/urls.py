"""es URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path, re_path

from django.contrib.sitemaps.views import sitemap
from .sitemaps import DocumentationSitemap, PartenaireSitemap, ProduitSitemap, \
    Entreprise_solutionSitemap, Artisans_solutionSitemap, Consultance_solutionSitemap, \
    TeamSitemap, StaticViewSitemap

sitemaps = {
    'documentation-view' : DocumentationSitemap,
    'partenaire-view' : PartenaireSitemap,
    'produit-view' : ProduitSitemap,
    'entreprise_solution-view' : Entreprise_solutionSitemap,
    'artisans_solution-view' : Artisans_solutionSitemap,
    'consultance_solution-view' : Consultance_solutionSitemap,
    'team-view' : TeamSitemap,
    'static': StaticViewSitemap,
    }

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('app/', include('app.urls')),
    path('', include('solutions.urls')),
    path('accounts/', include('accounts.urls')),
    path('produits/', include('produits.urls')),
    path('documentations/', include('documentations.urls')),
    path('partenaires/', include('partenaires.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('@es/', admin.site.urls),
    # path('newsletter/', include('newsletter.urls')),
    path('administration/', include('administration.urls')),
    path('tinymce/', include('tinymce.urls')),
    re_path('djga/', include('google_analytics.urls')),
]

handler400 = 'handlers.views.handler400'
handler403 = 'handlers.views.handler403'
handler404 = 'handlers.views.handler404'
handler500 = 'handlers.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

