from django.shortcuts import render
from search_views.search import SearchListView
# from search_views.filters import BaseFilter

from solutions.models import Entreprise_solution, Artisans_solution, Consultance_solution
# from solutions.forms import EntrepriseSearchForm
# Create your views here.

# class Entreprise_solutionFilter(BaseFilter):
#     search_fields = {
#         'search_text' : ['nom', 'secteur_entreprise', 'fonctions_entreprise'],
#         'search_telephone_entreprise_exact' : { 'operator' : '__exact', 'fields' : ['telephone_entreprise'] },
#         'search_telephone_entreprise_min' : { 'operator' : '__gte', 'fields' : ['telephone_entreprise'] },
#         'search_telephone_entreprise_max' : { 'operator' : '__lte', 'fields' : ['telephone_entreprise'] },
#     }

def search(request):        
    if request.method == 'POST':      
        book_name =  request.POST.getlist('search')      
        try:
            status = Add_prod.objects.filter(bookname__icontains=book_name)
            #Add_prod class contains a column called 'bookname'
        except Add_prod.DoesNotExist:
            status = None
        return render(request,"search.html", {"books":status})
    else:
        return render(request,"search.html",{})



def entreprise_solution_view(request):
    """
    docstring
    """
    context = {}
    template_name = 'pages/solutions/entreprise_solutions/entreprise_solutions.html'
    return render(request, template_name, context)


def entreprise_solutions_detail(request, slug):
    """
    docstring
    """
    entreprise_solutions = Entreprise_solution.objects.get(slug=slug)
    context = {
        'entreprise_solutions': entreprise_solutions
    }
    template_name = 'pages/solutions/entreprise_solutions/entreprise_solutions_detail.html'
    return render(request, template_name, context)



def artisans_solution_view(request):
    """
    artisans_solution_view
    """
    context = {}
    template_name = 'pages/solutions/artisans_solution/artisans_solution.html'
    return render(request, template_name, context)


def artisans_solution_detail(request, slug):
    """
    artisans_solution_detail
    """
    artisans_solution = Artisans_solution.objects.get(slug=slug)
    context = {
        'artisans_solution': artisans_solution
    }
    template_name = 'pages/solutions/artisans_solution/artisans_solution_detail.html'
    return render(request, template_name, context)



def consultant_solution_view(request):
    """
    consultant_solution
    """
    context = {}
    template_name = 'pages/solutions/consultant_solution/consultant_solution.html'
    return render(request, template_name, context)


def consultant_solution_detail(request, slug):
    """
    consultant_solution
    """
    consultance_solution = Consultance_solution.objects.get(slug=slug)
    context = {
        'consultance_solution': consultance_solution
    }
    template_name = 'pages/solutions/consultant_solution/consultant_solution_detail.html'
    return render(request, template_name, context)

