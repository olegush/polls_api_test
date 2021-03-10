from datetime import datetime

from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

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


class VoteViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Vote.objects.filter().order_by('-date')
    serializer_class = VoteSerializer
    # allowed_methods = ['GET', 'POST']

    # def get_queryset(self):
    #     return Vote.objects.filter().order_by('-date')
    #
    # # def list(self, request, *args, **kwargs):
    # #     return HttpResponse(content='')
    #
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

