from django.shortcuts import render
from .models import Tournament


def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournament/tournament.html', {'tournaments': tournaments})