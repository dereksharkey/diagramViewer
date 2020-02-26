from rest_framework import viewsets

from diagram.models import Diagram, Layer
from diagram.serializers import DiagramSerializer
from diagram.permissions import TempPermission

class DiagramViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides the 'list', 'create', 'retrieve', 'update' and 'destroy' actions
    """

    queryset = Diagram.objects.all()
    serializer_class = DiagramSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, TempPermission]
