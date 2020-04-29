from django.db import models

DIAGRAM_CHOICES = [
        ('netadmin', 'Network Administration'),
        ('sysadmin', 'Systems Administration'),
        ('av', 'Audio Visual Technology'),
        ('dcs', 'Desktop Support'),
        ('training', 'Training')
]

LAYER_CHOICES = [
        ('power', 'Power'),
        ('data', 'Data'),
        ('physical', 'Physical'),
        ('other', 'Other')
]

class Diagram(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    diagram_type = models.CharField(max_length=10, choices=DIAGRAM_CHOICES)

class Layer(models.Model):
    def __str__(self):
        return self.image.name
    def directory_path(instance, filename):
        return '{0}/{1}'.format(instance.diagram.name, filename)
    diagram = models.ForeignKey(Diagram, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=directory_path, blank=True, null=True)
