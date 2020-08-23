# -*- coding: utf-8 -*-

import unittest
from decimal import Decimal

from scripts.probability import roll_success_range

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class Test1d6StartZero(unittest.TestCase):
    """
    Tests the success range with the range [0,5], which is the range of a six sides die.
    """

    def test_below_min_above_not_equal(self):

        chance = roll_success_range(0, 5, -1, above=True, equal=False, normalize=True)

        self.assertEqual({"min": 0, "max": 5}, chance)

    def test_goal_2_above_not_equal(self):

        chance = roll_success_range(0, 5, 2, above=True, equal=False, normalize=True)

        self.assertEqual({"min": 0, "max": 2}, chance)

    def test_goal_2_above_equal(self):

        chance = roll_success_range(0, 5, 2, above=True, equal=True, normalize=True)

        self.assertEqual({"min": 0, "max": 3}, chance)

    def test_goal_2_below_not_equal(self):

        chance = roll_success_range(0, 5, 2, above=False, equal=False, normalize=True)

        self.assertEqual({"min": 0, "max": 1}, chance)

    def test_goal_2_below_equal(self):

        chance = roll_success_range(0, 5, 2, above=False, equal=True, normalize=True)

        self.assertEqual({"min": 0, "max": 2}, chance)


class Test1d6AboveNotEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,6], which is the range of a six sides die.
    """

    def test_no_goal(self):

        chance = roll_success_range(1, 6, 0, above=True, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 6}, chance)

    def test_goal_above_max(self):

        chance = roll_success_range(1, 6, 10, above=True, equal=False, normalize=True)

        self.assertEqual(None, chance)

    def test_goal_1(self):

        chance = roll_success_range(1, 6, 1, above=True, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 5}, chance)

    def test_goal_2(self):

        chance = roll_success_range(1, 6, 2, above=True, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 4}, chance)

    def test_goal_3(self):

        chance = roll_success_range(1, 6, 3, above=True, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 3}, chance)

    def test_goal_4(self):

        chance = roll_success_range(1, 6, 4, above=True, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 2}, chance)

    def test_goal_5(self):

        chance = roll_success_range(1, 6, 5, above=True, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 1}, chance)

    def test_goal_6(self):

        chance = roll_success_range(1, 6, 6, above=True, equal=False, normalize=True)

        self.assertEqual(None, chance)


class Test1d6AboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,6], which is the range of a six sides die.
    """

    def test_no_goal(self):

        chance = roll_success_range(1, 6, 0, above=True, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 6}, chance)

    def test_goal_above_max(self):

        chance = roll_success_range(1, 6, 10, above=True, equal=True, normalize=True)

        self.assertEqual(None, chance)

    def test_goal_1(self):

        chance = roll_success_range(1, 6, 1, above=True, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 6}, chance)

    def test_goal_2(self):

        chance = roll_success_range(1, 6, 2, above=True, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 5}, chance)

    def test_goal_3(self):

        chance = roll_success_range(1, 6, 3, above=True, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 4}, chance)

    def test_goal_4(self):

        chance = roll_success_range(1, 6, 4, above=True, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 3}, chance)

    def test_goal_5(self):

        chance = roll_success_range(1, 6, 5, above=True, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 2}, chance)

    def test_goal_6(self):

        chance = roll_success_range(1, 6, 6, above=True, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 1}, chance)


class Test1d6BelowNotEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,6], which is the range of a six sides die.
    """

    def test_no_goal(self):

        chance = roll_success_range(1, 6, 0, above=False, equal=False, normalize=True)

        self.assertEqual(None, chance)

    def test_goal_above_max(self):

        chance = roll_success_range(1, 6, 10, above=False, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 6}, chance)

    def test_goal_1(self):

        chance = roll_success_range(1, 6, 1, above=False, equal=False, normalize=True)

        self.assertEqual(None, chance)

    def test_goal_2(self):

        chance = roll_success_range(1, 6, 2, above=False, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 1}, chance)

    def test_goal_3(self):

        chance = roll_success_range(1, 6, 3, above=False, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 2}, chance)

    def test_goal_4(self):

        chance = roll_success_range(1, 6, 4, above=False, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 3}, chance)

    def test_goal_5(self):

        chance = roll_success_range(1, 6, 5, above=False, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 4}, chance)

    def test_goal_6(self):

        chance = roll_success_range(1, 6, 6, above=False, equal=False, normalize=True)

        self.assertEqual({"min": 1, "max": 5}, chance)


class Test1d6BelowEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,6], which is the range of a six sides die.
    """

    def test_no_goal(self):

        chance = roll_success_range(1, 6, 0, above=False, equal=True, normalize=True)

        self.assertEqual(None, chance)

    def test_goal_above_max(self):

        chance = roll_success_range(1, 6, 10, above=False, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 6}, chance)

    def test_goal_1(self):

        chance = roll_success_range(1, 6, 1, above=False, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 1}, chance)

    def test_goal_2(self):

        chance = roll_success_range(1, 6, 2, above=False, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 2}, chance)

    def test_goal_3(self):

        chance = roll_success_range(1, 6, 3, above=False, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 3}, chance)

    def test_goal_4(self):

        chance = roll_success_range(1, 6, 4, above=False, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 4}, chance)

    def test_goal_5(self):

        chance = roll_success_range(1, 6, 5, above=False, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 5}, chance)

    def test_goal_6(self):

        chance = roll_success_range(1, 6, 6, above=False, equal=True, normalize=True)

        self.assertEqual({"min": 1, "max": 6}, chance)
