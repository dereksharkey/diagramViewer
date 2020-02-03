from django.db import models

from diagram.models import Diagram

class Symptom(models.Model):
    diagram = models.ForeignKey(Diagram, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    issue = models.TextField()
    solution = models.TextField()
