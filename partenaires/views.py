from django.shortcuts import render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from partenaires.models import Partenaire
# Create your views here.
def partenaires_view(request):
    """
    docstring
    """
    partenaire = Partenaire.objects.all().order_by('-created')
    paginator = Paginator(partenaire, 12)
    page = request.GET.get('page')
    try:
        partenaire_list = paginator.page(page)
    except PageNotAnInteger:
        partenaire_list = paginator.page(1)
    except EmptyPage:
        partenaire_list = paginator.page(paginator.num_pages)
    context = {
        'partenaire_list': partenaire_list
    }
    template_name = 'pages/partenaires/partenaires.html'
    return render(request, template_name, context)
