from api.repositories import RepositoryQuestionary, RepositoryQuestion, RepositoryOption

class QuestionaryService:
    def __init__(self):
        self.repository = RepositoryQuestionary()

    def list_questionary(self, id_questionary=None):
        if id_questionary is not None:
            try:
                return self.repository.get_questionary_by_id(id_questionary)
            except self.repository.model.DoesNotExist:
                return None 
        else:
            return self.repository.list()
    
    def create_questionary(self, data):
        if "name_questionary" not in data or "description" not in data or "Author" not in data:
            raise ValueError("El título , la descripción y el Autor son obligatorios.")
        return self.repository.create_questionary(**data)
    
    def update_questionary(self, questionary, data):
        if not questionary:
            raise ValueError("Cuestionario no encontrado para modificar.")
        return self.repository.update_questionary(questionary, data)
    
    def delete_questionary(self, questionary_id):
        questionary = self.repository.get_questionary_by_id(questionary_id)
        if questionary:
            return self.repository.delete_questionary(questionary)
        raise ValueError("Cuestionario no encontrado para eliminar.")
    
class QuestionService:
    def __init__(self):
        self.repository_question = RepositoryQuestion()
    
    def list_question(self, id_question=None):
        if id_question is not None:
            try:
                return self.repository_question.get_question_by_id(id_question)
            except self.repository_question.model.DoesNotExist:
                return None 
        else:
            return self.repository_question.list()
        
    def create_question(self, data):
        if "question" not in data or "image_question" not in data:
            raise ValueError("La pregunta y la imagen son obligatorios.")
        return self.repository_question.create_question(**data)
    
    def update_question(self, question, data):
        if not question:
            raise ValueError("Pregunta no encontrada para modificar.")
        return self.repository_question.update_question(question, data)
    
    def delete_question(self, question_id):
        question = self.repository_question.get_question_by_id(question_id)
        if question:
            return self.repository_question.delete_question(question)
        raise ValueError("Pregunta no encontrada para eliminar.")
    
class OptionService:
    def __init__(self):
        self.repository_option = RepositoryOption()
    
    def list_option(self, id_option=None):
        if id_option is not None:
            try:
                return self.repository_option.get_option_by_id(id_option)
            except self.repository_option.model.DoesNotExist:
                return None 
        else:
            return self.repository_option.list()
        
    def create_option(self, data):
        if "descriptionOp" not in data: 
            raise ValueError("El texto de la opción es obligatorio.")
        return self.repository_option.create_option(**data)
    
    def update_option(self, option, data):
        if not option:
            raise ValueError("Opción no encontrada para modificar.")
        return self.repository_option.update_option(option, data)
    
    def delete_option(self, option_id):
        option = self.repository_option.get_option_by_id(option_id)
        if option:
            return self.repository_option.delete_option(option)
        raise ValueError("Opción no encontrada para eliminar.")
    
    