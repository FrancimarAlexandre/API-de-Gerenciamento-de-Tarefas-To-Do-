from django.shortcuts import render
from .serializers import TarefaSerializer
from .models import Tarefa
from rest_framework import viewsets
# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
