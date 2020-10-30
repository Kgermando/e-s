from django.shortcuts import render

from produits.models import Produit
# Create your views here.
def produits_view(request):
    """
    docstring
    """
    context = {}
    template_name = 'pages/produits/produits.html'
    return render(request, template_name, context)

def products_detail(request, slug):
    """
    docstring
    """
    docs_view = Documentation.objects.get(slug=slug)
    context = {
        'docs_view': docs_view
    }
    template_name = 'pages/docs/doc_detail.html'
    return render(request, template_name, context)
