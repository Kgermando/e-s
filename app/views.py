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
        if len(first_name)<3 or len(last_name)<3 or len(email_id)<5 or len(phone_num)<10 or len(message)<10:
            messages.error(request,'Svp, remplissez les champs correctement')
        else:
            contact_us = ContactForm(first_name=first_name,last_name=last_name,objet_name=objet_name,email_id=email_id,phone_num=phone_num,message=message)
            contact_us.save()
            # send_mail(first_name, )
            messages.success(request, 'Merci! Nous avons réçu votre message')
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