from rest_framework import serializers

from .models import Tarefa

class TarefaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarefa
        fields = "__all__"