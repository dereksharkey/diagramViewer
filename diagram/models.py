from django.db import models

class Diagram(models.Model):
    name = models.CharField()
    description = models.TextField()

class NetAdminDiagram(Diagram):
    comp_name = models.CharField()

class SysAdminDiagram(Diagram):
    comp_name = models.CharField()

class DSDiagram(Diagram):
    comp_name = models.CharField()

class AVTechDiagram(Diagram):
    comp_name = models.CharField()

class TrainingDiagram(Diagram):
    comp_name = models.CharField()
