from django.shortcuts import render, redirect
from django.contrib import messages # for message

from app.models import ContactForm, Team
# Create your views here.
def home_view(request):
    """
    docstring
    """
    context = {}
    template_name = 'pages/app/home.html'
    return render(request, template_name, context)

def contact_view(request):
    if  request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        objet_name = request.POST['objet_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        message = request.POST['message']
        #print(first_name,last_name,objet_name,email_id,phone_num,message)
        contact_us = ContactForm(first_name=first_name,last_name=last_name,objet_name=objet_name,email_id=email_id,phone_num=phone_num,message=message)
        contact_us.save()
        # send_mail(first_name, )
        messages.success(request,'! Nous avons réçu votre message')
        return redirect('/app/contact')

    template_name = 'pages/app/contact.html'
    return render(request, template_name, context=None)


def about_view(request):
    """
    A Propos de ES
    """
    team_list = Team.objects.all().order_by('-created')
    context = {
        'team_list': team_list
    }
    template_name = "pages/app/about.html"
    return render(request, template_name, context)


def historique_view(request):
    """
    Historique ES
    """
    context = {}
    template_name = "pages/app/historique.html"
    return render(request, template_name, context)

def about_detail(request, slug):
    """
        Product detail
    """
    produit = Produit.objects.get(slug=slug)
    context = {
        'produit': produit
    }
    template_name = 'pages/app/about.html'
    return render(request, template_name, context)


# def newsletter(request):
#     if  request.method == 'POST':
#         email = request.POST['email']
#         contact_us = Newsletter(email=email)
#         contact_us.save()
#         # send_mail(first_name, )
#         messages.success(request,'! Nous avons réçu votre email')
#         return redirect('')

#     template_name = 'nav/footer.html'
#     return render(request, template_name, context=None)
    