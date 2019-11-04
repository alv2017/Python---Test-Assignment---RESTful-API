from rest_framework import serializers
from geneapi.models import GeneAPI

class GeneAPISerializer(serializers.Serializer):
    id = serializers.CharField(source='stable_id', required=True, max_length=128)
    name = serializers.CharField(source='display_label', required=True, max_length=128)
    species = serializers.CharField(required=True, max_length=255)
    
    class Meta:
        model = GeneAPI
        fields = ('id', 'name', 'species')
        
        

    