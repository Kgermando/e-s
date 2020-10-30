from django.urls import path

from solutions.views import entreprise_solution_view, entreprise_solutions_detail, artisans_solution_view, artisans_solution_detail, consultant_solution_view, consultant_solution_detail

app_name = 'solutions'

urlpatterns = [
    path('', entreprise_solution_view, name='entreprise_solution'),
    path('entreprise_solution/<slug:slug>/', entreprise_solutions_detail, name='entreprise_solutions_detail'),
    path('artisans_solution/', artisans_solution_view, name='artisans_solution'),
    path('artisans_solution_detail/<slug:slug>/', artisans_solution_detail, name='artisans_solution_detail'),
    path('consultant_solution/', consultant_solution_view, name='consultant_solution'),
    path('consultant_solution_detail/<slug:slug>/', consultant_solution_detail, name='consultant_solution_detail'),
]
