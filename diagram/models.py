from django.db import models

DIAGRAM_CHOICES = [
        ('netadmin', 'Network Administration'),
        ('sysadmin', 'Systems Administration'),
        ('av', 'Audio Visual Technology'),
        ('dcs', 'Desktop Support'),
        ('training', 'Training')
]

LAYER_CHOICES = [
        ('power', ''),
        ('data', ''),
        ('physical', '')
]

class Diagram(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    diagram_type = models.CharField(max_length=10, choices=DIAGRAM_CHOICES)

class Layer(models.Model):
    diagram = models.ForeignKey(Diagram, on_delete=models.CASCADE)
    layer_type = models.CharField(max_length=100, choices=LAYER_CHOICES)
    image = models.FileField()
