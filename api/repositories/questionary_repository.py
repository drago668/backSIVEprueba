from api.models import Questionary, Question, Option

class RepositoryQuestionary:
    def list(self):
        return Questionary.objects.all()
    
    def get_questionary_by_id(self,id_questionary):
        try:
            return Questionary.objects.get(id_questionary=id_questionary)
        except Questionary.DoesNotExist:
            return None
        
    def create_questionary(self,**kwargs):
        questionary = Questionary(**kwargs)
        questionary.save()
        return questionary

    def update_questionary(self,questionary, *args, **kwargs):
        if questionary:
            for key, value in kwargs.items():
                setattr(questionary, key, value)
            questionary.save()
            return questionary
        return None
    
    
    def delete_questionary(self,questionary):
        if questionary:
            questionary.delete()
            return True
        return False
    
class RepositoryQuestion:
    def list(self):
        return Question.objects.all()
    
    def get_question_by_id(self,id_question):
        try:
            return Question.objects.get(id_question=id_question)
        except Question.DoesNotExist:
            return None
        
    def create_question(self,**kwargs):
        question = Question(**kwargs)
        question.save()
        return question

    def update_question(self,question, *args, **kwargs):
        if question:
            for key, value in kwargs.items():
                setattr(question, key, value)
            question.save()
            return question
        return None
    
    
    def delete_question(self,question):
        if question:
            question.delete()
            return True
        return False

class RepositoryOption:
    def list(self):
        return Option.objects.all()
    
    def get_option_by_id(self,id_option):
        try:
            return Option.objects.get(id_option=id_option)
        except Option.DoesNotExist:
            return None
        
    def create_option(self,**kwargs):
        option = Option(**kwargs)
        option.save()
        return option

    def update_option(self,option, *args, **kwargs):
        if option:
            for key, value in kwargs.items():
                setattr(option, key, value)
            option.save()
            return option
        return None
    
    
    def delete_option(self,option):
        if option:
            option.delete()
            return True
        return False