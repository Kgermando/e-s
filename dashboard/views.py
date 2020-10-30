from django.shortcuts import render

# Create your views here.

def dashboard_view(request):
    
    context = {}
    template_name = 'pages/dashboard/dashboard.html'
    return render(request, template_name, context)

def dashboard_forms_entreprise(request):
    
    context = {}
    template_name = 'pages/dashboard/forms_entreprise.html'
    return render(request, template_name, context)

def dashboard_forms_artisans(request):
    
    context = {}
    template_name = 'pages/dashboard/forms_artisans.html'
    return render(request, template_name, context)


def dashboard_forms_consultant(request):
    
    context = {}
    template_name = 'pages/dashboard/forms_consultant.html'
    return render(request, template_name, context)


def dashboard_forms_partenaire(request):
    
    context = {}
    template_name = 'pages/dashboard/forms_partenaire.html'
    return render(request, template_name, context)


def dashboard_forms_investisseurs(request):
    
    context = {}
    template_name = 'pages/dashboard/forms_investisseurs.html'
    return render(request, template_name, context)


def dashboard_opportunites(request):
    
    context = {}
    template_name = 'pages/dashboard/opportunites.html'
    return render(request, template_name, context)

def dashboard_annonces(request):
    
    context = {}
    template_name = 'pages/dashboard/annonces.html'
    return render(request, template_name, context)

def dashboard_fidelites(request):
    
    context = {}
    template_name = 'pages/dashboard/fidelites.html'
    return render(request, template_name, context)


def dashboard_marketing(request):
    
    context = {}
    template_name = 'pages/dashboard/marketing.html'
    return render(request, template_name, context)


def dashboard_commerciale(request):
    
    context = {}
    template_name = 'pages/dashboard/commerciale.html'
    return render(request, template_name, context)

