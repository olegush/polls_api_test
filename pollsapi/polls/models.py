from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=200)
    date_begin = models.DateTimeField('begin date')
    date_end = models.DateTimeField('end date')
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ManyToManyField(Poll, related_name='questions')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ManyToManyField(Question, related_name='answers')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    date = models.DateTimeField('date polled')
