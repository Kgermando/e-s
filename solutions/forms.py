from django import forms

class EntrepriseSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search nameet secteur_consultance, fonctions_consultance, description_consultance, competence_consultance',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )


class ArtisansSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search nameet secteur_consultance, fonctions_consultance, description_consultance, competence_consultance',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )


class ConsultanceSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search nameet secteur_consultance, fonctions_consultance, description_consultance, competence_consultance',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )
