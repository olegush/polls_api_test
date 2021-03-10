from datetime import datetime

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Poll, Vote
from .serializers import PollSerializer, VoteSerializer, VoteCreateSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.filter(
        date_end__gt=datetime.now()
    ).order_by('-date_begin')
    serializer_class = PollSerializer
    allowed_methods = ['GET']


class VoteViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    serializer_classes = {
        'create': VoteCreateSerializer,
        'retrieve': VoteSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)

    def retrieve(self, request, *args, **kwargs):
        votes = Vote.objects.filter(user=kwargs['pk']).order_by('-date')
        serializer = self.get_serializer(votes, many=True)
        return Response({'data': serializer.data})

