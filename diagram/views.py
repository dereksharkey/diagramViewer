from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ParseError

from diagram.models import Diagram, Layer
from diagram.serializers import DiagramSerializer, LayerSerializer
from diagram.permissions import TempPermission

class DiagramViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides the 'list', 'create', 'retrieve', 'update' and 'destroy' actions
    """

    queryset = Diagram.objects.all()
    serializer_class = DiagramSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, TempPermission]
    parser_class = (MultiPartParser, FormParser)

class LayerViewSet(viewsets.ModelViewSet):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
