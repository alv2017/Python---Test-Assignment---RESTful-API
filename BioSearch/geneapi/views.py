
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from django.core.exceptions import EmptyResultSet
from geneapi.models import GeneAPI
from geneapi.serializers import GeneAPISerializer


@api_view(['GET'])
def get_gene_by_name(request, name):
    """
        You can search gene details by typing in first n characters of the gene name.
        If you type in 1 or 2 characters, only exact gene name matches will be returned.
        If you type in 3 or more characters, all genes with names that start 
        with typed in characters will be displayed.
    """
    name = name.strip()
    if len(name) > 0 and len(name) < 3:
        try:
            data_objects = GeneAPI.objects.filter(display_label=name)
            if len(data_objects) == 0:
                raise EmptyResultSet
        except EmptyResultSet:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif len(name) >= 3:       
        try:
            data_objects = GeneAPI.objects.filter(
                Q(display_label__istartswith=name),
            )
            if len(data_objects) == 0:
                raise EmptyResultSet
        except EmptyResultSet:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        objects_serializer = GeneAPISerializer(data_objects, many=True)
        return Response(objects_serializer.data)
    
@api_view(['GET'])
def get_gene_by_name_and_species(request, name, species):
    """
        You can search gene details by typing in first n characters of the gene name
        and providing an exact species name. If you specify 1 or 2 characters
        of the gene name, only exact species with exact name matches will be returned. 
        If you type in 3 or more characters of the gene name, the search
        will return the names of the genes for the provided species,
        that start with the characters that you typed in as a gene name parameter.
        
    """
    name = name.strip()
    if len(name) > 0 and len(name) < 3:
        try:
            data_objects = GeneAPI.objects.filter(display_label=name, species=species)
            if len(data_objects) == 0:
                raise EmptyResultSet
        except EmptyResultSet:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif len(name) >= 3:       
        try:
            data_objects = GeneAPI.objects.filter(
                Q(display_label__istartswith=name),
                Q(species=species),
            )
            if len(data_objects) == 0:
                raise EmptyResultSet
        except EmptyResultSet:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        objects_serializer = GeneAPISerializer(data_objects, many=True)
        return Response(objects_serializer.data)  
    


