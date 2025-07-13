from __future__ import annotations

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    players = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.name