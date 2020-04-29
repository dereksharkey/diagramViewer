from rest_framework import serializers

from diagram.models import Diagram, Layer

class LayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Layer
        fields = '__all__'

class DiagramSerializer(serializers.HyperlinkedModelSerializer):
    layer_set = LayerSerializer(many=True, read_only=True)

    def create(self, validated_data):
        layers_data = self.context['request'].FILES
        diagram = Diagram.objects.create(
            name = validated_data.get('name'),
            description = validated_data.get('description'),
            diagram_type = validated_data.get('diagram_type')
        )
        for layer_data in layers_data.getlist('file'):
            Layer.objects.create(
                diagram=diagram, 
                image=layer_data
            )
        return diagram

    class Meta:
        model = Diagram
        fields = ('name', 'description', 'diagram_type', 'layer_set') 
