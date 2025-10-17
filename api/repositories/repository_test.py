from api.models import Test

class RepositoryTest:
    def list(self):
        return Test.objects.all()

    def get_test_by_id(self, id_test):
        try:
            return Test.objects.get(id_test=id_test)
        except Test.DoesNotExist:
            return None

    def create_test(self, **kwargs):
        test_instance = Test(**kwargs)
        test_instance.save()
        return test_instance

    def delete_test(self, test_instance):
        if test_instance:
            test_instance.delete()
            return True
        return False
