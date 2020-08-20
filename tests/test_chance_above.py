# -*- coding: utf-8 -*-

import unittest
from decimal import Decimal

from scripts.probability import chance_above

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestMinValues(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
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


class TestZeroToTen(unittest.TestCase):
    """
    Tests the chance to go above with the range [0,10].
    """

    def test_no_armor(self):
        """
        With no armor it always damages.
        """
        chance = chance_above(0, 10, 0)

        self.assertEqual(1, chance)

    def test_armor_at_max(self):
        """
        When the armor is at the max point the chance is 0%.
        """
        chance = chance_above(0, 10, 10)

        self.assertEqual(0, chance)

    def test_armor_at_middle(self):
        """
        When the armor is at the middle point the chance is around 50%.
        """
        chance = chance_above(0, 10, 5)

        self.assertEqual(Decimal('0.5454545454545454545454545455'), chance)

    def test_armor_close_to_max(self):
        """
        Verifies result when the armor is close to max.
        """
        chance = chance_above(0, 10, 8)

        self.assertEqual(Decimal('0.2727272727272727272727272727'), chance)

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

        self.assertEqual(Decimal('0.6363636363636363636363636364'), chance)

    def test_armor_just_below_max(self):
        """
        Verifies result when the armor is just below the max.
        """
        chance = chance_above(0, 10, 9)

        self.assertEqual(Decimal('0.1818181818181818181818181818'), chance)


class TestOneToTen(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,10].
    """

    def test_no_armor(self):
        """
        With no armor it always damages.
        """
        chance = chance_above(1, 10, 0)

        self.assertEqual(1, chance)

    def test_armor_at_max(self):
        """
        When the armor is at the max point the chance is 0%.
        """
        chance = chance_above(1, 10, 10)

        self.assertEqual(0, chance)

    def test_armor_at_min(self):
        """
        Verifies result when the armor is at the min max.
        """
        chance = chance_above(1, 10, 1)

        self.assertEqual(Decimal('0.9'), chance)

    def test_armor_at_middle(self):
        """
        When the armor is at the middle point the chance is around 50%.
        """
        chance = chance_above(1, 10, 5)

        self.assertEqual(Decimal('0.5'), chance)

    def test_armor_close_to_max(self):
        """
        Verifies result when the armor is close to max.
        """
        chance = chance_above(1, 10, 8)

        self.assertEqual(Decimal('0.2'), chance)

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

        self.assertEqual(Decimal('0.6'), chance)

    def test_armor_just_below_max(self):
        """
        Verifies result when the armor is just below the max.
        """
        chance = chance_above(1, 10, 9)

        self.assertEqual(Decimal('0.1'), chance)


class TestTenToOneHundred(unittest.TestCase):
    """
    Tests the chance to go above with the range [10,100].
    """

    def test_no_armor(self):
        """
        With no armor it always damages.
        """
        chance = chance_above(10, 100, 0)

        self.assertEqual(1, chance)

    def test_armor_at_max(self):
        """
        When the armor is at the max point the chance is 0%.
        """
        chance = chance_above(10, 100, 100)

        self.assertEqual(0, chance)

    def test_armor_at_min(self):
        """
        Verifies result when the armor is at the min max.
        """
        chance = chance_above(10, 100, 10)

        self.assertEqual(Decimal('0.8901098901098901098901098901'), chance)

    def test_armor_at_middle(self):
        """
        When the armor is at the middle point the chance is around 50%.
        """
        chance = chance_above(10, 100, 50)

        self.assertEqual(Decimal('0.4505494505494505494505494505'), chance)

    def test_armor_close_to_max(self):
        """
        Verifies result when the armor is close to max.
        """
        chance = chance_above(10, 100, 80)

        self.assertEqual(Decimal('0.1208791208791208791208791209'), chance)

    def test_armor_above_max(self):
        """
        Verifies result when the armor is above the max.
        """
        chance = chance_above(10, 100, 200)

        self.assertEqual(0, chance)

    def test_armor_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = chance_above(10, 100, 40)

        self.assertEqual(Decimal('0.5604395604395604395604395604'), chance)

    def test_armor_just_below_max(self):
        """
        Verifies result when the armor is just below the max.
        """
        chance = chance_above(10, 100, 90)

        self.assertEqual(Decimal('0.0109890109890109890109890110'), chance)
