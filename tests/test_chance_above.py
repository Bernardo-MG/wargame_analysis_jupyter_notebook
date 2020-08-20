# -*- coding: utf-8 -*-

import unittest

from scripts.probability import chance_above

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestMinValues(unittest.TestCase):
    """
    Tests the chance to damage with minimal values.
    """

    def test_zeros(self):
        """
        Zero values means zero chance.
        """
        chance = chance_above(0, 0, 0)

        self.assertEqual(0, chance)

    def test_min(self):
        """
        The min values means zero chance.
        """
        chance = chance_above(1, 1, 1)

        self.assertEqual(0, chance)

    def test_no_armor(self):
        """
        With no armor it always damages.
        """
        chance = chance_above(1, 1, 0)

        self.assertEqual(1, chance)


class TestZeroFloor(unittest.TestCase):
    """
    Tests the chance to damage with a damage range starting at 0.
    """

    def test_no_armor(self):
        """
        With no armor it always damages.
        """
        chance = chance_above(0, 10, 0)

        self.assertEqual(1, chance)

    def test_armor_at_middle(self):
        """
        When the armor is at the middle point the chance is around 50%.
        """
        chance = chance_above(0, 10, 5)

        self.assertEqual(0.4, chance)

    def test_armor_at_max(self):
        """
        When the armor is at the max point the chance is 0%.
        """
        chance = chance_above(0, 10, 10)

        self.assertEqual(0, chance)

    def test_armor_close_to_max(self):
        """
        Verifies result when the armor is close to max.
        """
        chance = chance_above(0, 10, 8)

        self.assertEqual(0.1, chance)

    def test_armor_above_max(self):
        """
        Verifies result when the armor is above the max.
        """
        chance = chance_above(0, 10, 20)

        self.assertEqual(0, chance)

    def test_armor_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = chance_above(0, 10, 4)

        self.assertEqual(0.5, chance)

    def test_armor_just_below_max(self):
        """
        Verifies result when the armor is just below the max.
        """
        chance = chance_above(0, 10, 9)

        self.assertEqual(0, chance)


class TestOneFloor(unittest.TestCase):
    """
    Tests the chance to damage with a damage range starting at 1.
    """

    def test_no_armor(self):
        """
        With no armor it always damages.
        """
        chance = chance_above(1, 10, 0)

        self.assertEqual(1, chance)

    def test_armor_at_min(self):
        """
        Verifies result when the armor is at the min max.
        """
        chance = chance_above(1, 10, 0)

        self.assertEqual(1, chance)

    def test_armor_at_middle(self):
        """
        When the armor is at the middle point the chance is around 50%.
        """
        chance = chance_above(1, 10, 5)

        self.assertEqual(0.4444444444444444, chance)

    def test_armor_at_max(self):
        """
        When the armor is at the max point the chance is 0%.
        """
        chance = chance_above(1, 10, 10)

        self.assertEqual(0, chance)

    def test_armor_close_to_max(self):
        """
        Verifies result when the armor is close to max.
        """
        chance = chance_above(1, 10, 8)

        self.assertEqual(0.1111111111111111, chance)

    def test_armor_above_max(self):
        """
        Verifies result when the armor is above the max.
        """
        chance = chance_above(1, 10, 20)

        self.assertEqual(0, chance)

    def test_armor_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = chance_above(1, 10, 4)

        self.assertEqual(0.5555555555555556, chance)

    def test_armor_just_below_max(self):
        """
        Verifies result when the armor is just below the max.
        """
        chance = chance_above(1, 10, 9)

        self.assertEqual(0, chance)
