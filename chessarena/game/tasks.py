from celery import shared_task
from .models import Game
from datetime import timedelta
from django.utils import timezone


@shared_task
def purge_abandoned_games() -> None:
    cutoff = timezone.now() - timedelta(hours=24)
    Game.objects.filter(created__lt=cutoff, pgn='').delete()