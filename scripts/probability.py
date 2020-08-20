import numpy as np
from decimal import Decimal


def at_least_one_hit(to_hit, max_shots):
    """
    Returns the chance to get at least one hit if the turns is spent shooting.
    """
    accuracy = to_hit
    if accuracy > 1:
        accuracy = 1
    chance = 1 - (1 - accuracy) ** max_shots
    return float(np.complex128(chance))


def roll_chance(floor, ceiling, goal, above=True, equal=False):
    """
    Returns the chance to get a value above the goal. This is the same as rolling a dice and trying to get above a
    value.
    """

    if ceiling == 0:
        chance = 0
    elif goal > ceiling:
        chance = 0
    elif goal < floor:
        chance = 1
    else:
        if equal:
            chance = (goal - 1) / Decimal(ceiling - floor + 1)
        else:
            chance = goal / Decimal(ceiling - floor + 1)

        if chance > 1:
            chance = 1
        elif chance < 0:
            chance = 0

        if above:
            # Success is the inverse of the chance to fail
            chance = 1 - Decimal(chance)
        else:
            chance = Decimal(chance)

    return chance
