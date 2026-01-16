from rest_framework.decorators import api_view
from .serializers import TarefaSerializer
from .models import Tarefa
from rest_framework import viewsets


# Create your views here.
class TarefaViewset(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
