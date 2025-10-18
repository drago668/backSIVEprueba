from api.models import Optical

class RepositoryOptical:
    def list(self):
        return Optical.objects.all()
    
    def get_optical_by_id(self,id_optical):
        try:
            return Optical.objects.get(id_optical=id_optical)
        except Optical.DoesNotExist:
            return None
        
    def create_optical(self,**kwargs):
        optical = Optical(**kwargs)
        optical.save()
        return optical

    def update_optical(self,optical, *args, **kwargs):
        if optical:
            for key, value in kwargs.items():
                setattr(optical, key, value)
            optical.save()
            return optical
        return None
    
    
    def delete_optical(self,optical):
        if optical:
            optical.delete()
            return True
        return False

