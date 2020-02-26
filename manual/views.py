from rest_framework import viewsets, renderers

from manual.models import Symptom
from manual.serializer import SymptomSerializer

class SymptomViewSet(viewsets.ModelViewSet):

    queryset = Syptom.objects.all()
    serializer_class = SymptomSerializer
