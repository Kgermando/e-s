from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Vous êtes maintenant authentifié! Allez dans Formulaire \
             pour ajouter votre Entreprise, Artisans, Consultant, partenaire et Investisseur ")
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, "les informations d'identification invalides, vérifier votre prénom")
            return redirect('login')
    return render(request, 'pages/accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        # Get form vales
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        # statut = request.POST['statut']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Ce Nom d\'utilisateur existe déjà!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Cette email est déjà utilisé!')
                    return redirect('register')
                else:
                    #Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, "You are now loged in")
                    # return redirect('index')

                    user.save()
                    messages.success(request, 'Congratulations! Vous êtes enregistrée! Connectez vous maintenant')
                    return redirect('login')
        else:
            messages.error(request, 'Le mot de passe ne corresponds pas')
            return redirect('register')
    else:
        return render(request, 'pages/accounts/register.html')
    
    return render(request, 'pages/accounts/register.html')

def logout_view(request):
    if request.method == 'GET':
        auth.logout(request)
        messages.success(request, "Vous êtes déconnecté.")
        return redirect('login')
    else:
        return redirect('solutions:entreprise_solution')



