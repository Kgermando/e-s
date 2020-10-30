from django.shortcuts import render

from documentations.models import Documentation
# Create your views here.
def doc_view(request):
    """
    All docs
    """
    doc_list = Documentation.objects.all()
    solutions_list = Documentation.objects.filter(categorie='SOLUTIONS')
    produits_list = Documentation.objects.filter(categorie='PRODUITS')
    partenaires_list = Documentation.objects.filter(categorie='PARTENAIRES')
    investisseurs_list = Documentation.objects.filter(categorie='INVESTISSEURS')
    context = {
        "doc_list": doc_list,
        "solutions_list": solutions_list,
        "produits_list": produits_list,
        "partenaires_list": partenaires_list,
        "investisseurs_list": investisseurs_list,
    }
    template_name = 'pages/docs/docs.html'
    return render(request, template_name, context)

def doc_view_detail(request, slug):
    """
    Vue detail de la documentation
    """
    docs_view = Documentation.objects.get(slug=slug)
    context = {
        'docs_view': docs_view
    }
    template_name = 'pages/docs/doc_detail.html'
    return render(request, template_name, context)

 