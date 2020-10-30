from django.shortcuts import render

# Create your views here.
def partenaires_view(request):
    """
    docstring
    """
    context = {}
    template_name = 'pages/partenaires/partenaires.html'
    return render(request, template_name, context)
