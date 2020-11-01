from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from solutions.models import Entreprise_solution, Artisans_solution, Consultance_solution

# Create your views here.

def entreprise_solution_search(request):
    query = request.GET.get('q', '')
    #The empty string handles an empty "request"
    if query:
            queryset = (Q(nom__icontains=query)| Q(secteur_entreprise__icontains=query)| Q(description_entreprise__icontains=query)| Q(competence_entreprise__icontains=query))
            results = Entreprise_solution.objects.filter(queryset).distinct()
    else:
        results = []

    context = {
        'results': results,
        'query': query
    }
    template_name = 'pages/solutions/entreprise_solutions/entreprise_solutions.html'
    return render(request, template_name, context)


def entreprise_solutions_detail(request, id):
    """
    entreprise_solution_ detail
    """
    entreprise = Entreprise_solution.objects.get(id=id)
    context = {
        'entreprise': entreprise
    }
    template_name = 'pages/solutions/entreprise_solutions/entreprise_solutions_detail.html'
    return render(request, template_name, context)



def artisans_solution_search(request):
    query = request.GET.get('q', '')
    #The empty string handles an empty "request"
    if query:
            queryset = (Q(nom__icontains=query)| Q(secteur_artisans__icontains=query)| Q(description_artisans__icontains=query)| Q(competence_artisans__icontains=query))
            results = Artisans_solution.objects.filter(queryset).distinct()
    else:
        results = []

    context = {
        'results': results,
        'query': query
    }
    template_name = 'pages/solutions/artisans_solution/artisans_solution.html'
    return render(request, template_name, context)


def artisans_solution_detail(request, id):
    """
        artisans_solution_detail
    """
    artisans_solution = Artisans_solution.objects.get(id=id)
    context = {
        'artisans_solution': artisans_solution
    }
    template_name = 'pages/solutions/artisans_solution/artisans_solution_detail.html'
    return render(request, template_name, context)



def consultance_solution_search(request):
    query = request.GET.get('q', '')
    #The empty string handles an empty "request"
    if query:
            queryset = (Q(nom__icontains=query)| Q(secteur_consultance__icontains=query)| Q(description_consultance__icontains=query)| Q(competence_consultance__icontains=query))
            results = Consultance_solution.objects.filter(queryset).distinct()
    else:
        results = []

    context = {
        'results': results,
        'query': query
    }
    template_name = 'pages/solutions/artisans_solution/artisans_solution.html'
    return render(request, template_name, context)

def consultance_solution_detail(request, id):
    """
    consultance_solution_detail
    """
    consultance_solution = Consultance_solution.objects.get(id=id)
    context = {
        'consultance_solution': consultance_solution
    }
    template_name = 'pages/solutions/consultant_solution/consultant_solution_detail.html'
    return render(request, template_name, context)

