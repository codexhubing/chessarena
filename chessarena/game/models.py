from __future__ import annotations

import io
import chess.pgn
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Game(models.Model):
    white = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='white_games')
    black = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='black_games')
    created = models.DateTimeField(auto_now_add=True)
    rated = models.BooleanField(default=False)
    pgn = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.white} vs {self.black}"

    def board(self) -> chess.Board:
        game = chess.pgn.read_game(io.StringIO(self.pgn)) if self.pgn else chess.pgn.Game()
        return game.board()