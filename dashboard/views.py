from django.shortcuts import render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required


from dashboard.models import Forms_Entreprise, Forms_Artisans, Forms_Consultant, Forms_Partenaire, \
    Forms_Investisseur, Opportunite, Annonce, Fidelite, Marketing, Commerciale
# Create your views here.

@login_required(login_url='/accounts/login/')
def dashboard_stats(request):
    
    context = {}
    template_name = 'pages/dashboard/stats.html'
    return render(request, template_name, context)
    
@login_required(login_url='/accounts/login/')
def dashboard_forms_entreprise(request):
    if  request.method == 'POST':
        company = request.POST['company']
        secteur = request.POST['secteur']
        description = request.POST['description']
        email = request.POST['email']
        telephone = request.POST['telephone']
        telephone_2 = request.POST['telephone_2']
        logo = request.POST['logo']
        rccm = request.POST['rccm']
        id_nat = request.POST['id_nat']
        date = request.POST['date']
        adresse = request.POST['adresse']
        #print(first_name,last_name,objet_name,email_id,phone_num,message)
        if len(company)<3 or len(email)<3 or len(secteur)<5 or len(description)<10 or len(adresse)<10:
            messages.error(request,'Svp, remplissez les champs correctement')
        else:
            forms_entreprise = Forms_Entreprise(company=company, secteur=secteur, description=description, email=email, telephone=telephone, \
                telephone_2=telephone_2, logo=logo, rccm=rccm, id_nat=id_nat, date=date, adresse=adresse)
            forms_entreprise.save()
            # send_mail(first_name, )
            messages.success(request, 'Merci! Nous avons réçu votre Fiche')
            return redirect('/forms_entreprise')
    
    context = {}
    template_name = 'pages/dashboard/forms_entreprise.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def dashboard_forms_artisans(request):
    if  request.method == 'POST':
        company = request.POST['company']
        secteur = request.POST['secteur']
        description = request.POST['description']
        email = request.POST['email']
        telephone = request.POST['telephone']
        telephone_2 = request.POST['telephone_2']
        logo = request.POST['logo']
        date = request.POST['date']
        adresse = request.POST['adresse']
        #print(first_name,last_name,objet_name,email_id,phone_num,message)
        if len(company)<3 or len(email)<3 or len(secteur)<5 or len(description)<10 or len(adresse)<10:
            messages.error(request,'Svp, remplissez les champs correctement')
        else:
            forms_artisans = Forms_Artisans(company=company, secteur=secteur, description=description, email=email, telephone=telephone, \
                telephone_2=telephone_2, logo=logo, date=date, adresse=adresse)
            forms_artisans.save()
            # send_mail(first_name, )
            messages.success(request, 'Merci! Nous avons réçu votre Fiche')
            return redirect('/forms_artisans')
    context = {}
    template_name = 'pages/dashboard/forms_artisans.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def dashboard_forms_consultant(request):
    if  request.method == 'POST':
        company = request.POST['company']
        secteur = request.POST['secteur']
        specialite = request.POST['specialite']
        email = request.POST['email']
        telephone = request.POST['telephone']
        telephone_2 = request.POST['telephone_2']
        logo = request.POST['logo']
        date = request.POST['date']
        adresse = request.POST['adresse']
        #print(first_name,last_name,objet_name,email_id,phone_num,message)
        if len(company)<3 or len(email)<3 or len(secteur)<5 or len(adresse)<10:
            messages.error(request,'Svp, remplissez les champs correctement')
        else:
            forms_consultant = Forms_Consultant(company=company, secteur=secteur, specialite=specialite, email=email, telephone=telephone, \
                telephone_2=telephone_2, logo=logo, date=date, adresse=adresse)
            forms_consultant.save()
            # send_mail(first_name, )
            messages.success(request, 'Merci! Nous avons réçu votre Fiche')
            return redirect('/forms_consultant')
    
    context = {}
    template_name = 'pages/dashboard/forms_consultant.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def dashboard_forms_partenaire(request):
    if  request.method == 'POST':
        company = request.POST['company']
        type = request.POST['type']
        secteur = request.POST['secteur']
        description = request.POST['description']
        email = request.POST['email']
        telephone = request.POST['telephone']
        telephone_2 = request.POST['telephone_2']
        logo = request.POST['logo']
        adresse = request.POST['adresse']
        #print(first_name,last_name,objet_name,email_id,phone_num,message)
        if len(company)<3 or len(email)<3 or len(secteur)<5 or len(adresse)<10:
            messages.error(request,'Svp, remplissez les champs correctement')
        else:
            forms_partenaire = Forms_Partenaire(company=company, type=type, secteur=secteur, description=description, email=email, telephone=telephone, \
                telephone_2=telephone_2, logo=logo, adresse=adresse)
            forms_partenaire.save()
            # send_mail(first_name, )
            messages.success(request, 'Merci! Nous avons réçu votre Fiche')
            return redirect('/forms_partenaire')
    context = {}
    template_name = 'pages/dashboard/forms_partenaire.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def dashboard_forms_investisseurs(request):
    if  request.method == 'POST':
        company = request.POST['company']
        motivation = request.POST['motivation']
        secteur = request.POST['secteur']
        description = request.POST['description']
        email = request.POST['email']
        telephone = request.POST['telephone']
        telephone_2 = request.POST['telephone_2']
        logo = request.POST['logo']
        adresse = request.POST['adresse']
        #print(first_name,last_name,objet_name,email_id,phone_num,message)
        if len(company)<3 or len(email)<3 or len(secteur)<5 or len(adresse)<10:
            messages.error(request,'Svp, remplissez les champs correctement')
        else:
            forms_inestisseurs = Forms_Investisseur(company=company, motivation=motivation, secteur=secteur, description=description, email=email, telephone=telephone, \
                telephone_2=telephone_2, logo=logo, adresse=adresse)
            forms_inestisseurs.save()
            # send_mail(first_name, )
            messages.success(request, 'Merci! Nous avons réçu votre Fiche')
            return redirect('/forms_inestisseurs')
    context = {}
    template_name = 'pages/dashboard/forms_investisseurs.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def dashboard_opportunites(request):
    opportunite = Opportunite.objects.all().order_by('-created')
    paginator = Paginator(opportunite, 5)
    page = request.GET.get('page')
    try:
        opportunite_list = paginator.page(page)
    except PageNotAnInteger:
        opportunite_list = paginator.page(1)
    except EmptyPage:
        opportunite_list = paginator.page(paginator.num_pages)
    context = {
        'opportunite_list': opportunite_list
    }
    template_name = 'pages/dashboard/opportunites.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def dashboard_annonces(request):
    annonce = Annonce.objects.all().order_by('-created')
    paginator = Paginator(annonce, 5)
    page = request.GET.get('page')
    try:
        annonce_list = paginator.page(page)
    except PageNotAnInteger:
        annonce_list = paginator.page(1)
    except EmptyPage:
        annonce_list = paginator.page(paginator.num_pages)
    context = {
        'annonce_list': annonce_list
    }
    template_name = 'pages/dashboard/annonces.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def dashboard_fidelites(request):
    fidelite = Fidelite.objects.all().order_by('-created')
    paginator = Paginator(fidelite, 5)
    page = request.GET.get('page')
    try:
        fidelite_list = paginator.page(page)
    except PageNotAnInteger:
        fidelite_list = paginator.page(1)
    except EmptyPage:
        fidelite_list = paginator.page(paginator.num_pages)
    context = {
        'fidelite_list': fidelite_list
    }
    template_name = 'pages/dashboard/fidelites.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def dashboard_marketing(request):
    marketing = Marketing.objects.all().order_by('-created')
    paginator = Paginator(marketing, 5)
    page = request.GET.get('page')
    try:
        marketing_list = paginator.page(page)
    except PageNotAnInteger:
        marketing_list = paginator.page(1)
    except EmptyPage:
        marketing_list = paginator.page(paginator.num_pages)
    context = {
        'marketing_list': marketing_list
    }
    template_name = 'pages/dashboard/marketing.html'
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def dashboard_commerciale(request):
    commerciale = Commerciale.objects.all().order_by('-created')
    paginator = Paginator(commerciale, 5)
    page = request.GET.get('page')
    try:
        commerciale_list = paginator.page(page)
    except PageNotAnInteger:
        commerciale_list = paginator.page(1)
    except EmptyPage:
        commerciale_list = paginator.page(paginator.num_pages)
    context = {
        'commerciale_list': commerciale_list
    }
    template_name = 'pages/dashboard/commerciale.html'
    return render(request, template_name, context)

