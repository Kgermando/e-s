from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from documentations.models import Documentation
from partenaires.models import Partenaire
from produits.models import Produit
from solutions.models import Entreprise_solution, Artisans_solution, Consultance_solution
from app.models import Team

class DocumentationSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Documentation.objects.all()

class PartenaireSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Partenaire.objects.all()

class ProduitSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Produit.objects.all()

class Entreprise_solutionSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Entreprise_solution.objects.all()


class Artisans_solutionSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Artisans_solution.objects.all()


class Consultance_solutionSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Consultance_solution.objects.all()


class TeamSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Team.objects.all()

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['solutions:entreprise_solution', 'solutions:artisans_solution', 'solutions:consultant_solution', 'ourteam:about', 'app:contact', 'login', 'register']

    def location(self, item):
        return reverse(item)
