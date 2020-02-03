from django.db import models

SUBJECTS = {
        'n': 'Network Administration',
        's': 'Systems Administration',
        'a': 'Audio Visual Technology',
        'd': 'Desktop Support',
}

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    subject = models.CharField(choices=SUBJECTS)
    score = models.IntegerField()

class Question(models.Model):
    name = models.CharField()
    quiz = models.ManyToManyField(Quiz)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField()
