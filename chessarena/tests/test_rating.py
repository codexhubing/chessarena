from game.utils import elo_update


def test_elo_update_draw():
    a, b = elo_update(1200, 1200, 0.5)
    assert a == 1200 and b == 1200