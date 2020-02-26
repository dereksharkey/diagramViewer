from rest_framework import serializers

from diagram.models import Diagram, Layer

class DiagramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagram
        fields = ['name', 'description', 'diagram_type']
