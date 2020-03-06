from django.db import models
from django.utils.translation import gettext_lazy as _

class Quiz(models.Model):

    class Subject(models.TextChoices):
        NETADMIN = 'NA', _('Network Administration')
        SYSADMIN = 'SA', _('Systems Administration')
        AV = 'AV', _('Audio Visual Technology')
        DCS = 'DS', _('Desktop Support')
        TRAIN = 'TR', _('Training')

    name = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.CharField(max_length=2, choices=Subject.choices)
    score = models.IntegerField()

class Question(models.Model):
    name = models.CharField(max_length=100)
    quiz = models.ManyToManyField(Quiz)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField()
