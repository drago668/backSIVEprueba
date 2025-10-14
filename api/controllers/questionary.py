from api.models import Questionary, Question, Option
from rest_framework import serializers  
from api.services import  QuestionaryService, QuestionService, OptionService
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from api.serializers import QuestionaryCreateSerializers, QuestionaryListSerializers, QuestionCreateSerializers, QuestionListSerializers, OptionCreateSerializers, OptionListSerializers
class QuestionaryController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    create_serializer_class = QuestionaryCreateSerializers
    list_serializer_class = QuestionaryListSerializers
    queryset = Questionary.objects.all()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = QuestionaryService() 

    # GET → listar todas o una por id
    def get(self, request, *args, **kwargs):
        id_questionary = kwargs.get('pk', None)
        if id_questionary:
            # Llama al método específico para obtener por ID
            questionary = self.service.list_questionary(id_questionary) 
            if not questionary:
                return Response({"error": "Cuestionario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            # Usas tu serializador para un solo objeto (many=False por defecto)
            serializer = self.list_serializer_class(questionary)
            return Response(serializer.data)
        else:
            # Llama al método para obtener la lista completa
            questionarys = self.service.list_questionary()
            # Usas tu serializador para una lista de objetos (many=True)
            serializer = self.list_serializer_class(questionarys, many=True)
            return Response(serializer.data)

    # POST → crear nuevo cuestionario
    def post(self, request, *args, **kwargs):
        serializer = self.create_serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            # validated_data['Author'] = request.user
            try:
                questionary = self.service.create_questionary(validated_data)
                return Response(self.create_serializer_class(questionary).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT → actualizar cuestionario existente
    def patch(self, request, pk, *args, **kwargs):
        questionary_instance = self.service.list_questionary(pk)
        if not questionary_instance:
            return Response({"error": "Cuestionario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.create_serializer_class(
            questionary_instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            updated_questionary = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE → eliminar cuestionario existente
    def delete(self, request, pk, *args, **kwargs):
        questionary_instance = self.service.list_questionary(pk)
        if not questionary_instance:
            return Response({"error": "Cuestionario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        questionary_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class QuestionController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionListSerializers
    create_serializer_class = QuestionCreateSerializers
    list_serializer_class = QuestionListSerializers
    queryset = Question.objects.all()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = QuestionService()

    def get(self, request, *args, **kwargs):
        id_question = kwargs.get('pk', None)
        if id_question:
            question = self.service.list_question(id_question) 
            if not question:
                return Response({"error": "Pregunta no encontrada"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.create_serializer_class(question)
            return Response(serializer.data)
        else:
            questions = self.service.list_question()
            serializer = self.create_serializer_class(questions, many=True)
            return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        serializer = self.create_serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            try:
                question = self.service.create_question(validated_data)
                return Response(self.create_serializer_class(question).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, *args, **kwargs):
        question_instance = self.service.list_question(pk)
        if not question_instance:
            return Response({"error": "Pregunta no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.create_serializer_class(
            question_instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            updated_question = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        question_instance = self.service.list_question(pk)
        if not question_instance:
            return Response({"error": "Pregunta no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        question_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OptionController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OptionListSerializers
    create_serializer_class = OptionCreateSerializers
    list_serializer_class = OptionListSerializers
    queryset = Option.objects.all()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = OptionService()     

    def get(self, request, *args, **kwargs):
        id_option = kwargs.get('pk', None)
        if id_option:
            option = self.service.list_option(id_option) 
            if not option:
                return Response({"error": "Opción no encontrada"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.create_serializer_class(option)
            return Response(serializer.data)
        else:
            options = self.service.list_option()
            serializer = self.create_serializer_class(options, many=True)
            return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        serializer = self.create_serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            try:
                option = self.service.create_option(validated_data)
                return Response(self.create_serializer_class(option).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, *args, **kwargs):
        option_instance = self.service.list_option(pk)
        if not option_instance:
            return Response({"error": "Opción no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.create_serializer_class(
            option_instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            updated_option = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        option_instance = self.service.list_option(pk)
        if not option_instance:
            return Response({"error": "Opción no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        option_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)