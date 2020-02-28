from django.db import models

DIAGRAM_CHOICES = []
LAYER_CHOICES = []

class Diagram(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    diagram_type = models.CharField(choices=DIAGRAM_CHOICES)

class Layer(models.Model):
    diagram = models.ForeignKey(Diagram, on_delete=models.CASCADE)
    layer_type = models.CharField(choices=LAYER_CHOICES)
    image = models.FileField()
