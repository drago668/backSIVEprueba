from api.models import Catalogue

class CatalogueRepository:
    def list(self):
        return Catalogue.objects.all()
    
    def get_catalogue_by_id(self, id_catalogue):
        try:
            return Catalogue.objects.get(id_catalogue=id_catalogue)
        except Catalogue.DoesNotExist:
            return None
        
    def create_catalogue(self, **kwargs):
        catalogue = Catalogue(**kwargs)
        catalogue.save()
        return catalogue

    def update_catalogue(self, catalogue, *args, **kwargs):
        if catalogue:
            for key, value in kwargs.items():
                setattr(catalogue, key, value)
            catalogue.save()
            return catalogue
        return None
    
    
    def delete_catalogue(self, catalogue):
        if catalogue:
            catalogue.delete()
            return True
        return False