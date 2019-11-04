from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Q
from ...models import GeneAPI
from ...serializers import GeneAPISerializer


# initialize the APIClient app
client = Client()

class GetGeneByNameTest(TestCase):
    """ Test module for GET gene by name method"""
    databases = {'default','geneapi'}
    
    def setUp(self):
        self.name = 'aabr0700100'
        self.name_notvalid = 'notvalid'

    def test_get_gene_by_name_existing_item(self):
        response = client.get(
            reverse('get_gene_by_name', kwargs={'name': self.name}))
        gene = GeneAPI.objects.filter(
                Q(display_label__istartswith=self.name),
            )
        serializer = GeneAPISerializer(gene, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_get_gene_by_name_nonexisting_item(self):
        response = client.get(
            reverse('get_gene_by_name', kwargs={'name': self.name_notvalid}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    
    
    
    
