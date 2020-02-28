from rest_framework import serializers

from manual.models import Symptom

class SymptomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symptom
        fields = ['name', 'description', 'issue', 'solution', 'diagram']
