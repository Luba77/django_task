from rest_framework import generics

from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer


class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

