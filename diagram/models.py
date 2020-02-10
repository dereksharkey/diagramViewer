from django.db import models

class Diagram(models.Model):
    name = models.CharField()
    description = models.TextField()
    diagram_type = models.CharField()

class Layer(models.Model):
    diagram = models.ForeignKey(Diagram, on_delete=CASCADE)
    layer_type = models.CharField()
    image = models.FileField()
