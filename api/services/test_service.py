from api.repositories import RepositoryTest

class TestService:
    def __init__(self):
        self.repository = RepositoryTest()

    def list_tests(self):
        return self.repository.list()
    
    def get_test_by_id(self, test_id):
        return self.repository.get_test_by_id(test_id)
    
    def create_test(self, data):
        return self.repository.create_test(**data)
    
    def delete_test(self, test_id):
        test_instance = self.repository.get_test_by_id(test_id)
        if test_instance:
            return self.repository.delete_test(test_instance)
        raise ValueError("Test no encontrado para eliminar.")