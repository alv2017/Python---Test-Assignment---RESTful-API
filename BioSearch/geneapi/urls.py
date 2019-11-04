from django.urls import path
from geneapi import views

urlpatterns = [
    path('gene/<name>/', views.get_gene_by_name, name='get_gene_by_name'),
    path('gene/<name>/<species>/', views.get_gene_by_name_and_species, 
         name='get_gene_by_name_and_species'),
]