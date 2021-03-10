from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Poll(models.Model):
    name = models.CharField(max_length=200)
    date_begin = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)
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
    user = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote_answers = models.ManyToManyField(Answer, related_name='vote_answers')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'user #{self.user} : {self.poll} : {self.question} : ' \
               f'{self.vote_answers} : {self.date}'
