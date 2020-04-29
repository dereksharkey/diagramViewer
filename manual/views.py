from rest_framework import viewsets, renderers

from manual.models import Symptom
from manual.serializers import SymptomSerializer

class SymptomViewSet(viewsets.ModelViewSet):

    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
