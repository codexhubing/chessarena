from rest_framework import serializers
from game.models import Game
from tournament.models import Tournament


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'white', 'black', 'rated', 'pgn']


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'name', 'players']