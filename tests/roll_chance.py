# -*- coding: utf-8 -*-

import unittest
from decimal import Decimal

from scripts.probability import roll_chance

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestMinValuesAboveNotEqual(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
    """

    def test_zeros(self):
        """
        Zero values means zero chance.
        """
        chance = roll_chance(0, 0, 0, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_min(self):
        """
        The min values means zero chance.
        """
        chance = roll_chance(1, 1, 1, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_no_goal(self):
        """
        With no goal it always damages.
        """
        chance = roll_chance(1, 1, 0, above=True, equal=False)

        self.assertEqual(1, chance)


class TestZeroToTenAboveNotEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [0,10].
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = roll_chance(0, 10, 0, above=True, equal=False)

        self.assertEqual(1, chance)

    def test_goal_at_max(self):
        """
        When the goal is at the max point the chance is 0%.
        """
        chance = roll_chance(0, 10, 10, above=True, equal=False)

        self.assertEqual(Decimal('0.0909090909090909090909090909'), chance)

    def test_goal_at_middle(self):
        """
        When the goal is at the middle point the chance is around 50%.
        """
        chance = roll_chance(0, 10, 5, above=True, equal=False)

        self.assertEqual(Decimal('0.5454545454545454545454545455'), chance)

    def test_goal_close_to_max(self):
        """
        Verifies result when the goal is close to max.
        """
        chance = roll_chance(0, 10, 8, above=True, equal=False)

        self.assertEqual(Decimal('0.2727272727272727272727272727'), chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = roll_chance(0, 10, 20, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_goal_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = roll_chance(0, 10, 4, above=True, equal=False)

        self.assertEqual(Decimal('0.6363636363636363636363636364'), chance)

    def test_goal_just_below_max(self):
        """
        Verifies result when the goal is just below the max.
        """
        chance = roll_chance(0, 10, 9, above=True, equal=False)

        self.assertEqual(Decimal('0.1818181818181818181818181818'), chance)


class TestOneToTenAboveNotEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,10].
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = roll_chance(1, 10, 0, above=True, equal=False)

        self.assertEqual(1, chance)

    def test_goal_at_max(self):
        """
        When the goal is at the max point the chance is 0%.
        """
        chance = roll_chance(1, 10, 10, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_goal_at_min(self):
        """
        Verifies result when the goal is at the min max.
        """
        chance = roll_chance(1, 10, 1, above=True, equal=False)

        self.assertEqual(Decimal('0.9'), chance)

    def test_goal_at_middle(self):
        """
        When the goal is at the middle point the chance is around 50%.
        """
        chance = roll_chance(1, 10, 5, above=True, equal=False)

        self.assertEqual(Decimal('0.5'), chance)

    def test_goal_close_to_max(self):
        """
        Verifies result when the goal is close to max.
        """
        chance = roll_chance(1, 10, 8, above=True, equal=False)

        self.assertEqual(Decimal('0.2'), chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = roll_chance(1, 10, 20, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_goal_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = roll_chance(1, 10, 4, above=True, equal=False)

        self.assertEqual(Decimal('0.6'), chance)

    def test_goal_just_below_max(self):
        """
        Verifies result when the goal is just below the max.
        """
        chance = roll_chance(1, 10, 9, above=True, equal=False)

        self.assertEqual(Decimal('0.1'), chance)


class TestTenToOneHundredAboveNotEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [10,100].
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = roll_chance(10, 100, 0, above=True, equal=False)

        self.assertEqual(1, chance)

    def test_goal_at_max(self):
        """
        When the goal is at the max point the chance is 0%.
        """
        chance = roll_chance(10, 100, 100, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_goal_at_min(self):
        """
        Verifies result when the goal is at the min max.
        """
        chance = roll_chance(10, 100, 10, above=True, equal=False)

        self.assertEqual(Decimal('0.8901098901098901098901098901'), chance)

    def test_goal_at_middle(self):
        """
        When the goal is at the middle point the chance is around 50%.
        """
        chance = roll_chance(10, 100, 50, above=True, equal=False)

        self.assertEqual(Decimal('0.4505494505494505494505494505'), chance)

    def test_goal_close_to_max(self):
        """
        Verifies result when the goal is close to max.
        """
        chance = roll_chance(10, 100, 80, above=True, equal=False)

        self.assertEqual(Decimal('0.1208791208791208791208791209'), chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = roll_chance(10, 100, 200, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_goal_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = roll_chance(10, 100, 40, above=True, equal=False)

        self.assertEqual(Decimal('0.5604395604395604395604395604'), chance)

    def test_goal_just_below_max(self):
        """
        Verifies result when the goal is just below the max.
        """
        chance = roll_chance(10, 100, 90, above=True, equal=False)

        self.assertEqual(Decimal('0.0109890109890109890109890110'), chance)

    def test_goal_below_min(self):
        """
        When the goal is below the min the result is successful.
        """
        chance = roll_chance(10, 100, 5, above=True, equal=False)

        self.assertEqual(Decimal('1'), chance)

    def test_goal_just_below_min(self):
        """
        When the goal is just below the min the result is successful.
        """
        chance = roll_chance(10, 100, 9, above=True, equal=False)

        self.assertEqual(Decimal('1'), chance)


class Test1d6AboveNotEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,6], which is the range of a six sides die.
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = roll_chance(1, 6, 0, above=True, equal=False)

        self.assertEqual(1, chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = roll_chance(1, 6, 10, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_goal_1(self):
        """
        Verifies result when the goal is 1.
        """
        chance = roll_chance(1, 6, 1, above=True, equal=False)

        self.assertEqual(Decimal('0.8333333333333333333333333333'), chance)

    def test_goal_2(self):
        """
        Verifies result when the goal is 2.
        """
        chance = roll_chance(1, 6, 2, above=True, equal=False)

        self.assertEqual(Decimal('0.6666666666666666666666666667'), chance)

    def test_goal_3(self):
        """
        Verifies result when the goal is 3.
        """
        chance = roll_chance(1, 6, 3, above=True, equal=False)

        self.assertEqual(Decimal('0.5'), chance)

    def test_goal_4(self):
        """
        Verifies result when the goal is 4.
        """
        chance = roll_chance(1, 6, 4, above=True, equal=False)

        self.assertEqual(Decimal('0.3333333333333333333333333333'), chance)

    def test_goal_5(self):
        """
        Verifies result when the goal is 5.
        """
        chance = roll_chance(1, 6, 5, above=True, equal=False)

        self.assertEqual(Decimal('0.1666666666666666666666666667'), chance)

    def test_goal_6(self):
        """
        Verifies result when the goal is 6.
        """
        chance = roll_chance(1, 6, 6, above=True, equal=False)

        self.assertEqual(Decimal('0'), chance)


class TestMinValuesAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
    """

    def test_zeros(self):
        """
        Zero values means zero chance.
        """
        chance = roll_chance(0, 0, 0, above=True, equal=True)

        self.assertEqual(0, chance)

    def test_min(self):
        """
        The min values means zero chance.
        """
        chance = roll_chance(1, 1, 1, above=True, equal=True)

        self.assertEqual(1, chance)

    def test_no_goal(self):
        """
        With no goal it always damages.
        """
        chance = roll_chance(1, 1, 0, above=True, equal=True)

        self.assertEqual(1, chance)


class TestZeroToTenAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [0,10].
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = roll_chance(0, 10, 0, above=True, equal=True)

        self.assertEqual(1, chance)

    def test_goal_at_max(self):
        """
        When the goal is at the max point the chance is 0%.
        """
        chance = roll_chance(0, 10, 10, above=True, equal=True)

        self.assertEqual(Decimal('0.1818181818181818181818181818'), chance)

    def test_goal_at_middle(self):
        """
        When the goal is at the middle point the chance is around 50%.
        """
        chance = roll_chance(0, 10, 5, above=True, equal=True)

        self.assertEqual(Decimal('0.6363636363636363636363636364'), chance)

    def test_goal_close_to_max(self):
        """
        Verifies result when the goal is close to max.
        """
        chance = roll_chance(0, 10, 8, above=True, equal=True)

        self.assertEqual(Decimal('0.3636363636363636363636363636'), chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = roll_chance(0, 10, 20, above=True, equal=True)

        self.assertEqual(0, chance)

    def test_goal_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = roll_chance(0, 10, 4, above=True, equal=True)

        self.assertEqual(Decimal('0.7272727272727272727272727273'), chance)

    def test_goal_just_below_max(self):
        """
        Verifies result when the goal is just below the max.
        """
        chance = roll_chance(0, 10, 9, above=True, equal=True)

        self.assertEqual(Decimal('0.2727272727272727272727272727'), chance)


class TestOneToTenAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,10].
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = roll_chance(1, 10, 0, above=True, equal=True)

        self.assertEqual(1, chance)

    def test_goal_at_max(self):
        """
        When the goal is at the max point the chance is 0%.
        """
        chance = roll_chance(1, 10, 10, above=True, equal=True)

        self.assertEqual(Decimal('0.1'), chance)

    def test_goal_at_min(self):
        """
        Verifies result when the goal is at the min max.
        """
        chance = roll_chance(1, 10, 1, above=True, equal=True)

        self.assertEqual(Decimal('1'), chance)

    def test_goal_at_middle(self):
        """
        When the goal is at the middle point the chance is around 50%.
        """
        chance = roll_chance(1, 10, 5, above=True, equal=True)

        self.assertEqual(Decimal('0.6'), chance)

    def test_goal_close_to_max(self):
        """
        Verifies result when the goal is close to max.
        """
        chance = roll_chance(1, 10, 8, above=True, equal=True)

        self.assertEqual(Decimal('0.3'), chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = roll_chance(1, 10, 20, above=True, equal=True)

        self.assertEqual(0, chance)

    def test_goal_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = roll_chance(1, 10, 4, above=True, equal=True)

        self.assertEqual(Decimal('0.7'), chance)

    def test_goal_just_below_max(self):
        """
        Verifies result when the goal is just below the max.
        """
        chance = roll_chance(1, 10, 9, above=True, equal=True)

        self.assertEqual(Decimal('0.2'), chance)


class TestTenToOneHundredAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [10,100].
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = roll_chance(10, 100, 0, above=True, equal=True)

        self.assertEqual(1, chance)

    def test_goal_at_max(self):
        """
        When the goal is at the max point the chance is 0%.
        """
        chance = roll_chance(10, 100, 100, above=True, equal=True)

        self.assertEqual(0, chance)

    def test_goal_at_min(self):
        """
        Verifies result when the goal is at the min max.
        """
        chance = roll_chance(10, 100, 10, above=True, equal=True)

        self.assertEqual(Decimal('0.9010989010989010989010989011'), chance)

    def test_goal_at_middle(self):
        """
        When the goal is at the middle point the chance is around 50%.
        """
        chance = roll_chance(10, 100, 50, above=True, equal=True)

        self.assertEqual(Decimal('0.4615384615384615384615384615'), chance)

    def test_goal_close_to_max(self):
        """
        Verifies result when the goal is close to max.
        """
        chance = roll_chance(10, 100, 80, above=True, equal=True)

        self.assertEqual(Decimal('0.1318681318681318681318681319'), chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = roll_chance(10, 100, 200, above=True, equal=True)

        self.assertEqual(0, chance)

    def test_goal_just_below_middle(self):
        """
        Verifies result when just before middle point.
        """
        chance = roll_chance(10, 100, 40, above=True, equal=True)

        self.assertEqual(Decimal('0.5714285714285714285714285714'), chance)

    def test_goal_just_below_max(self):
        """
        Verifies result when the goal is just below the max.
        """
        chance = roll_chance(10, 100, 90, above=True, equal=True)

        self.assertEqual(Decimal('0.0219780219780219780219780220'), chance)

    def test_goal_below_min(self):
        """
        When the goal is below the min the result is successful.
        """
        chance = roll_chance(10, 100, 5, above=True, equal=True)

        self.assertEqual(Decimal('1'), chance)

    def test_goal_just_below_min(self):
        """
        When the goal is just below the min the result is successful.
        """
        chance = roll_chance(10, 100, 9, above=True, equal=True)

        self.assertEqual(Decimal('1'), chance)


class Test1d6AboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,6], which is the range of a six sides die.
    """

    def test_no_goal(self):
        """
        With no goal it always is successful.
        """
        chance = roll_chance(1, 6, 0, above=True, equal=True)

        self.assertEqual(1, chance)

    def test_goal_above_max(self):
        """
        Verifies result when the goal is above the max.
        """
        chance = roll_chance(1, 6, 10, above=True, equal=True)

        self.assertEqual(0, chance)

    def test_goal_1(self):
        """
        Verifies result when the goal is 1.
        """
        chance = roll_chance(1, 6, 1, above=True, equal=True)

        self.assertEqual(Decimal('1'), chance)

    def test_goal_2(self):
        """
        Verifies result when the goal is 2.
        """
        chance = roll_chance(1, 6, 2, above=True, equal=True)

        self.assertEqual(Decimal('0.8333333333333333333333333333'), chance)

    def test_goal_3(self):
        """
        Verifies result when the goal is 3.
        """
        chance = roll_chance(1, 6, 3, above=True, equal=True)

        self.assertEqual(Decimal('0.6666666666666666666666666667'), chance)

    def test_goal_4(self):
        """
        Verifies result when the goal is 4.
        """
        chance = roll_chance(1, 6, 4, above=True, equal=True)

        self.assertEqual(Decimal('0.5'), chance)

    def test_goal_5(self):
        """
        Verifies result when the goal is 5.
        """
        chance = roll_chance(1, 6, 5, above=True, equal=True)

        self.assertEqual(Decimal('0.3333333333333333333333333333'), chance)

    def test_goal_6(self):
        """
        Verifies result when the goal is 6.
        """
        chance = roll_chance(1, 6, 6, above=True, equal=True)

        self.assertEqual(Decimal('0.1666666666666666666666666667'), chance)
