from rest_framework import serializers

from solutions.models import Entreprise_solution, Artisans_solution, Consultance_solution

class EntrepriseSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise_solution
        fields = (
            'id', 'nom', 'secteur_entreprise', 'fonctions_entreprise', 'logo_entreprise',
            'telephone_entreprise', 'telephone_2_entreprise', 'email_entreprise', 'site_web',
            'description_entreprise', 'competence_entreprise', 'sociauFB_entreprise',
            'sociauTW_entreprise', 'sociauINS_entreprise', 'sociauIN_entreprise'
        )

        
class ArtisansSolutionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Artisans_solution
        fields = ( 
            'nom', 'secteur_artisans', 'fonctions_artisans', 'logo_artisans', 'telephone_artisans',
            'telephone_2_artisans', 'email_artisans', 'site_web', 'description_artisans', 'competence_artisans',
            'sociauFB_artisans', 'sociauTW_artisans', 'sociauINS_artisans', 'sociauIN_artisans'
        )
    
class ConsultanceSolutionserializer(serializers.ModelSerializer):
    class Meta: 
        model = Consultance_solution
        fields = (
            'nom', 'secteur_consultance', 'fonctions_consultance', 'fonctions_consultance', 'logo_consultance',
            'telephone_consultance', 'telephone_2_consultance', 'email_consultance', 'site_web', 'description_consultance',
            'competence_consultance', 'sociauFB_consultance', 'sociauTW_consultance', 'sociauINS_consultance',
            'sociauIN_consultance',
        )
