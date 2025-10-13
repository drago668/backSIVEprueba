from api.models import Questionary, Question, Option
from rest_framework import serializers  
from api.services import  QuestionaryService
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from api.serializers import QuestionaryCreateSerializers, QuestionaryListSerializers, QuestionCreateSerializers, OptionCreateSerializers

class QuestionaryController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    create_serializer_class = QuestionaryCreateSerializers
    list_serializer_class = QuestionaryListSerializers
    queryset = Questionary.objects.all()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = QuestionaryService() 
        
    def get_serializer_class(self):
        if self.action == 'create':
            return QuestionaryCreateSerializers
        return QuestionaryListSerializers

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
            validated_data['Author'] = request.user
            try:
                questionary = self.service.create_questionary(validated_data)
                return Response(self.create_serializer_class(questionary).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT → actualizar cuestionario existente
    def patch(self, request, pk, *args, **kwargs):
        try:
            questionary = self.service.update_questionary(pk)
            if not questionary:
                return Response({"error": "Cuestionario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except questionary.DoesNotExist:
            return Response({"error": "Cuestionario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
    

    