from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework import viewsets

from .models import Question, Poll, Vote
from .serializers import PollSerializer, VoteSerializer


class PollViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Poll.objects.filter(
        date_end__gt=datetime.now()
    ).order_by('-date_begin')
    serializer_class = PollSerializer
    allowed_methods = ['GET']


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.filter().order_by(
        '-date')
    serializer_class = VoteSerializer
    allowed_methods = ['GET', 'POST']
