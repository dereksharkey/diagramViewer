from django.db import models

from diagramViewer.diagram.models import diagram

class Symptom(models.Model):
    diagram = models.ForeignKey(diagram)
    name = models.CharField(max_length=100)
    description = models.TextField()
    issue = models.TextField()
    solution = models.TextField()
