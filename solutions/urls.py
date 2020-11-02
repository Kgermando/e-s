from django.urls import path

from solutions.views import entreprise_solution_search, entreprise_solutions_detail, \
    artisans_solution_search, artisans_solution_detail, \
    consultance_solution_search, consultance_solution_detail

app_name = 'solutions'

urlpatterns = [
    path('', entreprise_solution_search, name='entreprise_solution'),
    path('entreprise_solution/entreprise_solution/<int:id>/', entreprise_solutions_detail, name='entreprise_solutions_detail'),
    path('artisans_solution/', artisans_solution_search, name='artisans_solution'),
    path('artisans_solution/artisans_solution_detail/<int:id>/', artisans_solution_detail, name='artisans_solution_detail'),
    path('consultant_solution/', consultance_solution_search, name='consultant_solution'),
    path('consultant_solution/consultance_solutions_detail/<int:id>/', consultance_solution_detail, name='consultance_solutions_detail'),
]
