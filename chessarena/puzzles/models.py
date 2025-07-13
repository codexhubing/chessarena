from __future__ import annotations

from django.db import models


class Puzzle(models.Model):
    fen = models.CharField(max_length=100)
    solution = models.CharField(max_length=100)
    daily = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.fen