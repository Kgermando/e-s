from django.urls import path

from produits.views import produits_view, products_detail

app_name = 'produits'

urlpatterns = [
    path('', produits_view, name='produits'),
    path('produit_detail/<slug:slug>/', products_detail, name='product_detail'),
    path('produit_detail/<int:id>/', products_detail, name='product_detail_id'),
]
