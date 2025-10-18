from api.repositories import CatalogueRepository

class CatalogueService:
    def __init__(self):
        self.repository = CatalogueRepository()

    def list_catalogue(self):
        return self.repository.list()

    def get_catalogue(self, id_catalogue):
        return self.repository.get_catalogue_by_id(id_catalogue)

    def create_catalogue(self, data):
        if "nameP" not in data or "price" not in data:
            raise ValueError("El nombre y el precio son obligatorios.")
        return self.repository.create_catalogue(**data)

    def update_catalogue(self, catalogue, data):
        if not catalogue:
            raise ValueError("Catálogo no encontrado para modificar.")
        return self.repository.update_catalogue(catalogue, **data)

    def delete_catalogue(self, id_catalogue):
        catalogue = self.repository.get_catalogue_by_id(id_catalogue)
        if catalogue:
            return self.repository.delete_catalogue(catalogue)
        raise ValueError("Catálogo no encontrado para eliminar.")