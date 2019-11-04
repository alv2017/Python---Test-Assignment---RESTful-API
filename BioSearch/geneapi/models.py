from django.db import models

# Create your models here.
class GeneAPI(models.Model):
    stable_id = models.CharField(max_length=128, blank=False, primary_key=True)
    species = models.CharField(max_length=255, blank=False)
    display_label = models.CharField(max_length=255, blank=False)
    
    class Meta:
        managed = False
        db_table = 'gene_autocomplete'
        verbose_name = 'geneapi_model'

  

        
