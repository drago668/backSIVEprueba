from api.repositories import RepositoryOptical

class OpticalService:
    def __init__(self):
      self.repository = RepositoryOptical()


    def list_optical(self):
      return self.repository.list()

    def get_optical(self, optical_id):
      return self.repository.get_optical_by_id(optical_id)


    def create_optical(self, data):
      if "nameOp" not in data or "email" not in data or "address" not in data:
        raise ValueError("El nombre, el correo electrónico y dirección son obligatorios.")
      return self.repository.create_optical(**data)


    def update_optical(self, optical, data):
        if not optical:
            raise ValueError("Óptica no encontrada para modificar.")
        return self.repository.update_optical(optical, **data)


    def delete_optical(self, optical_id):
        optical = self.repository.get_optical_by_id(optical_id)
        if optical:
            return self.repository.delete_optical(optical)
        raise ValueError("Óptica no encontrada para eliminar.")
