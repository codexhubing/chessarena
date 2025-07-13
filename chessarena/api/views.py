from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from game.models import Game
from tournament.models import Tournament
from .serializers import GameSerializer, TournamentSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [IsAuthenticated]