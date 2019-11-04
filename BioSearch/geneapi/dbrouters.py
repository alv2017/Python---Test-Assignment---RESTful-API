import sys

class GeneAPIRouter:
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read geneapi models go to geneapi database
        """
        if model._meta.app_label == 'geneapi' and model._meta.verbose_name=='geneapi_model':
            return 'geneapi'
        
        return None
    


    
 
    
    