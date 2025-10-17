from api.repositories import RepositoryTest
from api.models import Questionary, User

class TestService:
    def __init__(self):
        self.repository = RepositoryTest()

    def list_tests(self):
        return self.repository.list()
    
    def get_test_by_id(self, test_id):
        return self.repository.get_test_by_id(test_id)
    
    def create_test(self, validated_data):
        try: 
            return self.repository.create_test(**validated_data)
        except Questionary.DoesNotExist:
            raise ValueError(f"Cuestionario con ID {validated_data["questionary_id"]} no encontrado.")
        except User.DoesNotExist:
            raise ValueError(f"Usuario con ID {validated_data["user_id"]} no encontrado.")
          
    def delete_test(self, test_id):
        test_instance = self.repository.get_test_by_id(test_id)
        if test_instance:
            return self.repository.delete_test(test_instance)
        raise ValueError("Test no encontrado para eliminar.")