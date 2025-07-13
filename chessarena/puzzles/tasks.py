from celery import shared_task
from .models import Puzzle


@shared_task
def generate_daily_puzzles() -> None:
    Puzzle.objects.update(daily=False)
    Puzzle.objects.order_by('?')[:3].update(daily=True)