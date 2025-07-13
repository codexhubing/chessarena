import pytest
from django.contrib.auth.models import User
from game.models import Game


@pytest.mark.django_db
def test_game_creation():
    user1 = User.objects.create(username='u1')
    user2 = User.objects.create(username='u2')
    game = Game.objects.create(white=user1, black=user2)
    assert str(game) == 'u1 vs u2'