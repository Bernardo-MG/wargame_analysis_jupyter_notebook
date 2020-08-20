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

    def test_no_goal(self):
        """
        With no goal it always damages.
        """
        chance = chance_above(1, 1, 0)

        self.assertEqual(1, chance)


class TestZeroToTen(unittest.TestCase):
    """
    Tests the chance to go above with the range [0,10].
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = chance_above(0, 10, 0)

        self.assertEqual(1, chance)

    def test_goal_at_max(self):
        """
        When the goal is at the max point the chance is 0%.
        """
        chance = chance_above(0, 10, 10)

        self.assertEqual(0, chance)

    def test_goal_at_middle(self):
        """
        When the goal is at the middle point the chance is around 50%.
        """
        chance = chance_above(0, 10, 5)

        self.assertEqual(Decimal('0.5454545454545454545454545455'), chance)

    def test_goal_close_to_max(self):
        """
        Verifies result when the goal is close to max.
        """
        chance = chance_above(0, 10, 8)

        self.assertEqual(Decimal('0.2727272727272727272727272727'), chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = chance_above(0, 10, 20)

        self.assertEqual(0, chance)

    def test_goal_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = chance_above(0, 10, 4)

        self.assertEqual(Decimal('0.6363636363636363636363636364'), chance)

    def test_goal_just_below_max(self):
        """
        Verifies result when the goal is just below the max.
        """
        chance = chance_above(0, 10, 9)

        self.assertEqual(Decimal('0.1818181818181818181818181818'), chance)


class TestOneToTen(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,10].
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = chance_above(1, 10, 0)

        self.assertEqual(1, chance)

    def test_goal_at_max(self):
        """
        When the goal is at the max point the chance is 0%.
        """
        chance = chance_above(1, 10, 10)

        self.assertEqual(0, chance)

    def test_goal_at_min(self):
        """
        Verifies result when the goal is at the min max.
        """
        chance = chance_above(1, 10, 1)

        self.assertEqual(Decimal('0.9'), chance)

    def test_goal_at_middle(self):
        """
        When the goal is at the middle point the chance is around 50%.
        """
        chance = chance_above(1, 10, 5)

        self.assertEqual(Decimal('0.5'), chance)

    def test_goal_close_to_max(self):
        """
        Verifies result when the goal is close to max.
        """
        chance = chance_above(1, 10, 8)

        self.assertEqual(Decimal('0.2'), chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = chance_above(1, 10, 20)

        self.assertEqual(0, chance)

    def test_goal_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = chance_above(1, 10, 4)

        self.assertEqual(Decimal('0.6'), chance)

    def test_goal_just_below_max(self):
        """
        Verifies result when the goal is just below the max.
        """
        chance = chance_above(1, 10, 9)

        self.assertEqual(Decimal('0.1'), chance)


class TestTenToOneHundred(unittest.TestCase):
    """
    Tests the chance to go above with the range [10,100].
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = chance_above(10, 100, 0)

        self.assertEqual(1, chance)

    def test_goal_at_max(self):
        """
        When the goal is at the max point the chance is 0%.
        """
        chance = chance_above(10, 100, 100)

        self.assertEqual(0, chance)

    def test_goal_at_min(self):
        """
        Verifies result when the goal is at the min max.
        """
        chance = chance_above(10, 100, 10)

        self.assertEqual(Decimal('0.8901098901098901098901098901'), chance)

    def test_goal_at_middle(self):
        """
        When the goal is at the middle point the chance is around 50%.
        """
        chance = chance_above(10, 100, 50)

        self.assertEqual(Decimal('0.4505494505494505494505494505'), chance)

    def test_goal_close_to_max(self):
        """
        Verifies result when the goal is close to max.
        """
        chance = chance_above(10, 100, 80)

        self.assertEqual(Decimal('0.1208791208791208791208791209'), chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = chance_above(10, 100, 200)

        self.assertEqual(0, chance)

    def test_goal_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = chance_above(10, 100, 40)

        self.assertEqual(Decimal('0.5604395604395604395604395604'), chance)

    def test_goal_just_below_max(self):
        """
        Verifies result when the goal is just below the max.
        """
        chance = chance_above(10, 100, 90)

        self.assertEqual(Decimal('0.0109890109890109890109890110'), chance)

    def test_goal_below_min(self):
        """
        When the goal is below the min the result is successful.
        """
        chance = chance_above(10, 100, 5)

        self.assertEqual(Decimal('1'), chance)

    def test_goal_just_below_min(self):
        """
        When the goal is just below the min the result is successful.
        """
        chance = chance_above(10, 100, 9)

        self.assertEqual(Decimal('1'), chance)


class Test1d6(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,6], which is the range of a six sides die.
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = chance_above(1, 6, 0)

        self.assertEqual(1, chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = chance_above(1, 6, 10)

        self.assertEqual(0, chance)

    def test_goal_1(self):
        """
        Verifies result when the goal is 1.
        """
        chance = chance_above(1, 6, 1)

        self.assertEqual(Decimal('0.8333333333333333333333333333'), chance)

    def test_goal_2(self):
        """
        Verifies result when the goal is 2.
        """
        chance = chance_above(1, 6, 2)

        self.assertEqual(Decimal('0.6666666666666666666666666667'), chance)

    def test_goal_3(self):
        """
        Verifies result when the goal is 3.
        """
        chance = chance_above(1, 6, 3)

        self.assertEqual(Decimal('0.5'), chance)

    def test_goal_4(self):
        """
        Verifies result when the goal is 4.
        """
        chance = chance_above(1, 6, 4)

        self.assertEqual(Decimal('0.3333333333333333333333333333'), chance)

    def test_goal_5(self):
        """
        Verifies result when the goal is 5.
        """
        chance = chance_above(1, 6, 5)

        self.assertEqual(Decimal('0.1666666666666666666666666667'), chance)

    def test_goal_6(self):
        """
        Verifies result when the goal is 6.
        """
        chance = chance_above(1, 6, 6)

        self.assertEqual(Decimal('0'), chance)

