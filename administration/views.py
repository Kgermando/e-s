from django.shortcuts import render

from dashboard.models import ( 
        Forms_Entreprise, 
        Forms_Artisans, 
        Forms_Consultant, 
        Forms_Partenaire, 
        Forms_Investisseur
    )
# Create your views here.
def forms_download(request):
    """
    docstring 
    """
    forms_entreprise = Forms_Entreprise.objects.all().order_by('-created')
    forms_artisans = Forms_Artisans.objects.all().order_by('-created')
    forms_consultant = Forms_Consultant.objects.all().order_by('-created')
    forms_partenaire = Forms_Partenaire.objects.all().order_by('-created')
    forms_investisseur = Forms_Investisseur.objects.all().order_by('-created')
    context = {
        'forms_entreprise': forms_entreprise,
        'forms_artisans': forms_artisans,
        'forms_consultant': forms_consultant,
        'forms_partenaire': forms_partenaire,
        'forms_investisseur': forms_investisseur,
    }
    template_name = 'pages/administration/admin-forms.html'
    return render(request, template_name, context)


