import numpy as np


def at_least_one_hit(to_hit, max_shots):
    """
    Returns the chance to get at least one hit if the turns is spent shooting.
    """
    accuracy = to_hit
    if accuracy > 1:
        accuracy = 1
    chance = 1 - (1 - accuracy) ** max_shots
    return float(np.complex128(chance))


def chance_above(floor, ceiling, gateway):
    """
    Returns the chance to get a value above the gateway.

    The values should follow a homogeneous distribution. Each number should have the same chance of being selected.
    """

    if ceiling == 0:
        chance = 0
    elif gateway == 0:
        chance = 1
    elif gateway >= ceiling:
        chance = 0
    elif gateway < floor:
        chance = 1
    else:
        # To ease handling the minimal damage we will normalize values
        max_norm = ceiling - floor
        gateway_norm = gateway - floor

        # The damage required to actually damage the target with 1 point
        lowest_valid = gateway_norm + 1
        # The number of damage values which can damage the target
        damage_range = max_norm - lowest_valid
        # Proportion of the full damage spectrum which can actually damage the target
        chance = damage_range / max_norm

        # Success is the inverse of the chance to fail
        # chance = 1- (gateway_norm + 1) / max_norm

    return chance
