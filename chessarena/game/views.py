from __future__ import annotations

from django.shortcuts import get_object_or_404, render
from .models import Game


def game_view(request, pk: int):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game/game.html', {'game': game})