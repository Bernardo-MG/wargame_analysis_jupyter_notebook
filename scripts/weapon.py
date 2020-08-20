import math


def max_shots(turn_tus, weapon_tus, reload_tu, burst, ammo):
    """
    Returns the max number of shots a weapon can achieve in a turn.

    Takes into consideration that the weapon may have to reload.
    """
    if ammo <= 0:
        shots = 0
    elif weapon_tus <= 0:
        shots = 0
    else:
        fire_actions = int(turn_tus / weapon_tus)
        shots = fire_actions * burst

        if shots > ammo:
            # Shoots above capacity. Has to reload

            # We need to check the number of times the weapon has to reload
            reload_shots = fire_actions
            if reload_shots > 1:
                # Adds cost to reload between shots
                reload_cost = (reload_shots - 1) * reload_tu
                # The cost will be averaged to each shot
                reload_cost = reload_cost / reload_shots
            else:
                # A single shot. No reload needed
                reload_cost = 0
            cost = weapon_tus + reload_cost
            fire_actions = int(turn_tus / cost)
            shots = fire_actions * burst

    return shots


def penetrating_damage(base_damage, armor):
    """
    Returns the damage after applying armor.
    """
    min_prop = 0
    max_prop = 2

    min_damage = min_prop * base_damage
    max_damage = max_prop * base_damage

    if armor >= max_damage:
        damage = 0
    elif armor < min_damage:
        damage = base_damage
    else:
        # To ease handling the minimal damage we will normalize values
        max_damage_norm = max_damage - min_damage
        armor_norm = armor - min_damage

        # The damage required to actually damage the target with 1 point
        lowest_valid_damage = armor_norm + 1
        # The number of damage values which can damage the target
        damage_range = max_damage_norm - lowest_valid_damage
        # Proportion of the full damage spectrum which can actually damage the target
        to_damage = damage_range / max_damage_norm
        #
        damage = damage_range * to_damage / 2

    return damage


def hits_to_kill(damage, health):
    """
    Returns the number of hits it takes to kill the target.
    """
    if damage > 0:
        hits = health / damage
    else:
        hits = 1000

    if hits < 1:
        hits = 1
    else:
        hits = math.ceil(hits)

    return hits
