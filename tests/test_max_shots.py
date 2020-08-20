# -*- coding: utf-8 -*-

import unittest

from scripts.weapon import max_shots

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestMinValues(unittest.TestCase):
    """
    Tests the max shots with minimal values.
    """

    def test_zeros(self):
        """
        Zero values means zero shots.
        """
        shots = max_shots(0, 0, 0, 0, 0)

        self.assertEqual(0, shots)

    def test_min(self):
        """
        The min values give one shot.
        """
        shots = max_shots(1, 1, 1, 1, 1)

        self.assertEqual(1, shots)

    def test_no_burst(self):
        """
        No burst means no shots.
        """
        shots = max_shots(1, 1, 1, 0, 1)

        self.assertEqual(0, shots)

    def test_no_ammo(self):
        """
        Can't shoot without ammo capacity.
        """
        shots = max_shots(1, 1, 1, 1, 0)

        self.assertEqual(0, shots)


class TestPercentileSingleShot(unittest.TestCase):
    """
    Tests the max shots with percentile values and burst of 1.
    """

    def test_full_turn(self):
        """
        Takes a full turn to shoot.
        """
        shots = max_shots(100, 100, 15, 1, 3)

        self.assertEqual(1, shots)

    def test_half_turn_enough_ammo(self):
        """
        Takes half a turn to shoot and has enough ammo for all the shots.
        """
        shots = max_shots(100, 50, 15, 1, 2)

        self.assertEqual(2, shots)

    def test_half_turn_more_than_enough_ammo(self):
        """
        Takes half a turn to shoot and has enough ammo to keep shooting.
        """
        shots = max_shots(100, 50, 15, 1, 3)

        self.assertEqual(2, shots)

    def test_half_turn_not_enough_ammo(self):
        """
        Takes half a turn to shoot and hasn't enough ammo for all the shots.
        """
        shots = max_shots(100, 50, 15, 1, 1)

        self.assertEqual(1, shots)


class TestPercentileTripleShot(unittest.TestCase):
    """
    Tests the max shots with percentile values and burst of 3.
    """

    def test_full_turn(self):
        """
        Takes a full turn to shoot.
        """
        shots = max_shots(100, 100, 15, 3, 9)

        self.assertEqual(3, shots)

    def test_half_turn_enough_ammo(self):
        """
        Takes half a turn to shoot and has enough ammo for all the shots.
        """
        shots = max_shots(100, 50, 15, 3, 6)

        self.assertEqual(6, shots)

    def test_half_turn_more_than_enough_ammo(self):
        """
        Takes half a turn to shoot and has enough ammo to keep shooting.
        """
        shots = max_shots(100, 50, 15, 3, 9)

        self.assertEqual(6, shots)

    def test_half_turn_not_enough_ammo(self):
        """
        Takes half a turn to shoot and hasn't enough ammo for all the shots.
        """
        shots = max_shots(100, 50, 15, 3, 3)

        self.assertEqual(3, shots)
