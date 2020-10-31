from django.shortcuts import render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from produits.models import Produit
# from produits.models import Innovation, Formation, Accompagnement, Consultant, \
#     Marketing, Communication, Immobilie, Transport, Assurance_et_finance
# Create your views here.
def produits_view(request):
    """
    Product list
    """
    produit = Produit.objects.all().order_by('created')
    paginator = Paginator(produit, 9)
    page = request.GET.get('page')
    try:
        produit_list = paginator.page(page)
    except PageNotAnInteger:
        produit_list = paginator.page(1)
    except EmptyPage:
        produit_list = paginator.page(paginator.num_pages)
    context = {
        'produit_list': produit_list
    }
    template_name = 'pages/produits/produits.html'
    return render(request, template_name, context)



def products_detail(request, slug):
    """
        Product detail
    """
    produit = Produit.objects.get(slug=slug)
    context = {
        'produit': produit
    }
    template_name = 'pages/produits/produit_detail.html'
    return render(request, template_name, context)

