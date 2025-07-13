from __future__ import annotations

from math import pow
from typing import Tuple


def elo_update(rating_a: int, rating_b: int, score_a: float, k: int = 32) -> Tuple[int, int]:
    expected_a = 1 / (1 + pow(10, (rating_b - rating_a) / 400))
    expected_b = 1 - expected_a
    new_a = rating_a + k * (score_a - expected_a)
    new_b = rating_b + k * ((1 - score_a) - expected_b)
    return round(new_a), round(new_b)