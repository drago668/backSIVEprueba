from api.models import Test, user
from api.models.questionary import Questionary
from api.models.user import User
from django.core.exceptions import ObjectDoesNotExist
class RepositoryTest:
    def list(self):
        return Test.objects.all()

    def get_test_by_id(self, id_test):
        try:
            return Test.objects.get(id_test=id_test)
        except Test.DoesNotExist:
            return None
    
    def get_questionary_by_id(self, id_questionary):
        return Questionary.objects.get(id_questionary=id_questionary)
    
    def get_user_by_id(self, id_user):
        return User.objects.get(id=id_user)
    
    def create_test(self, **test_Data):
        try:
            return Test.objects.create(**test_Data)
        except Exception as e:
            raise ObjectDoesNotExist("Error al crear el test")

    def delete_test(self, test_instance):
        if test_instance:
            test_instance.delete()
            return True
        return False
