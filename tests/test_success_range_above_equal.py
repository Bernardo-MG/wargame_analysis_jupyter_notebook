# -*- coding: utf-8 -*-

import unittest

from scripts.probability import roll_success_range

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestZeroToTenAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [0,10].
    """

    def test_goal_0(self):

        chance = roll_success_range(0, 10, 0, above=True, equal=True)

        self.assertEqual({"min": 0, "max": 10}, chance)

    def test_goal_1(self):

        chance = roll_success_range(0, 10, 1, above=True, equal=True)

        self.assertEqual({"min": 1, "max": 10}, chance)

    def test_goal_2(self):

        chance = roll_success_range(0, 10, 2, above=True, equal=True)

        self.assertEqual({"min": 2, "max": 10}, chance)

    def test_goal_3(self):

        chance = roll_success_range(0, 10, 3, above=True, equal=True)

        self.assertEqual({"min": 3, "max": 10}, chance)

    def test_goal_4(self):

        chance = roll_success_range(0, 10, 4, above=True, equal=True)

        self.assertEqual({"min": 4, "max": 10}, chance)

    def test_goal_5(self):

        chance = roll_success_range(0, 10, 5, above=True, equal=True)

        self.assertEqual({"min": 5, "max": 10}, chance)

    def test_goal_6(self):

        chance = roll_success_range(0, 10, 6, above=True, equal=True)

        self.assertEqual({"min": 6, "max": 10}, chance)

    def test_goal_7(self):

        chance = roll_success_range(0, 10, 7, above=True, equal=True)

        self.assertEqual({"min": 7, "max": 10}, chance)

    def test_goal_8(self):

        chance = roll_success_range(0, 10, 8, above=True, equal=True)

        self.assertEqual({"min": 8, "max": 10}, chance)

    def test_goal_9(self):

        chance = roll_success_range(0, 10, 9, above=True, equal=True)

        self.assertEqual({"min": 9, "max": 10}, chance)

    def test_goal_10(self):

        chance = roll_success_range(0, 10, 10, above=True, equal=True)

        self.assertEqual({"min": 10, "max": 10}, chance)

    def test_goal_above_max(self):

        chance = roll_success_range(0, 10, 20, above=True, equal=True)

        self.assertEqual(None, chance)

    def test_goal_below_min(self):

        chance = roll_success_range(0, 10, -1, above=True, equal=True)

        self.assertEqual({"min": 0, "max": 10}, chance)


class TestOneToTenAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,10].
    """

    def test_goal_1(self):

        chance = roll_success_range(1, 10, 1, above=True, equal=True)

        self.assertEqual({"min": 1, "max": 10}, chance)

    def test_goal_2(self):

        chance = roll_success_range(1, 10, 2, above=True, equal=True)

        self.assertEqual({"min": 2, "max": 10}, chance)

    def test_goal_3(self):

        chance = roll_success_range(1, 10, 3, above=True, equal=True)

        self.assertEqual({"min": 3, "max": 10}, chance)

    def test_goal_4(self):

        chance = roll_success_range(1, 10, 4, above=True, equal=True)

        self.assertEqual({"min": 4, "max": 10}, chance)

    def test_goal_5(self):

        chance = roll_success_range(1, 10, 5, above=True, equal=True)

        self.assertEqual({"min": 5, "max": 10}, chance)

    def test_goal_6(self):

        chance = roll_success_range(1, 10, 6, above=True, equal=True)

        self.assertEqual({"min": 6, "max": 10}, chance)

    def test_goal_7(self):

        chance = roll_success_range(1, 10, 7, above=True, equal=True)

        self.assertEqual({"min": 7, "max": 10}, chance)

    def test_goal_8(self):

        chance = roll_success_range(1, 10, 8, above=True, equal=True)

        self.assertEqual({"min": 8, "max": 10}, chance)

    def test_goal_9(self):

        chance = roll_success_range(1, 10, 9, above=True, equal=True)

        self.assertEqual({"min": 9, "max": 10}, chance)

    def test_goal_10(self):

        chance = roll_success_range(1, 10, 10, above=True, equal=True)

        self.assertEqual({"min": 10, "max": 10}, chance)

    def test_goal_above_max(self):

        chance = roll_success_range(1, 10, 20, above=True, equal=True)

        self.assertEqual(None, chance)

    def test_goal_below_min(self):

        chance = roll_success_range(1, 10, 0, above=True, equal=True)

        self.assertEqual({"min": 1, "max": 10}, chance)


class TestTenToOneHundredAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [10,100].
    """

    def test_no_goal(self):

        chance = roll_success_range(10, 100, 0, above=True, equal=True)

        self.assertEqual({"min": 10, "max": 100}, chance)

    def test_goal_at_max(self):

        chance = roll_success_range(10, 100, 100, above=True, equal=True)

        self.assertEqual({"min": 100, "max": 100}, chance)

    def test_goal_at_min(self):

        chance = roll_success_range(10, 100, 10, above=True, equal=True)

        self.assertEqual({"min": 10, "max": 100}, chance)

    def test_goal_at_middle(self):

        chance = roll_success_range(10, 100, 50, above=True, equal=True)

        self.assertEqual({"min": 50, "max": 100}, chance)

    def test_goal_close_to_max(self):

        chance = roll_success_range(10, 100, 80, above=True, equal=True)

        self.assertEqual({"min": 80, "max": 100}, chance)

    def test_goal_above_max(self):

        chance = roll_success_range(10, 100, 200, above=True, equal=True)

        self.assertEqual(None, chance)

    def test_goal_just_below_middle(self):

        chance = roll_success_range(10, 100, 40, above=True, equal=True)

        self.assertEqual({"min": 40, "max": 100}, chance)

    def test_goal_just_below_max(self):

        chance = roll_success_range(10, 100, 90, above=True, equal=True)

        self.assertEqual({"min": 90, "max": 100}, chance)

    def test_goal_below_min(self):

        chance = roll_success_range(10, 100, 5, above=True, equal=True)

        self.assertEqual({"min": 10, "max": 100}, chance)

    def test_goal_just_below_min(self):

        chance = roll_success_range(10, 100, 9, above=True, equal=True)

        self.assertEqual({"min": 10, "max": 100}, chance)


class Test1d6AboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,6], which is the range of a six sides die.
    """

    def test_no_goal(self):

        chance = roll_success_range(1, 6, 0, above=True, equal=True)

        self.assertEqual({"min": 1, "max": 6}, chance)

    def test_goal_above_max(self):

        chance = roll_success_range(1, 6, 10, above=True, equal=True)

        self.assertEqual(None, chance)

    def test_goal_1(self):

        chance = roll_success_range(1, 6, 1, above=True, equal=True)

        self.assertEqual({"min": 1, "max": 6}, chance)

    def test_goal_2(self):

        chance = roll_success_range(1, 6, 2, above=True, equal=True)

        self.assertEqual({"min": 2, "max": 6}, chance)

    def test_goal_3(self):

        chance = roll_success_range(1, 6, 3, above=True, equal=True)

        self.assertEqual({"min": 3, "max": 6}, chance)

    def test_goal_4(self):

        chance = roll_success_range(1, 6, 4, above=True, equal=True)

        self.assertEqual({"min": 4, "max": 6}, chance)

    def test_goal_5(self):

        chance = roll_success_range(1, 6, 5, above=True, equal=True)

        self.assertEqual({"min": 5, "max": 6}, chance)

    def test_goal_6(self):

        chance = roll_success_range(1, 6, 6, above=True, equal=True)

        self.assertEqual({"min": 6, "max": 6}, chance)


class Test1d6Norm0AboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with the range [1,6], which is the range of a six sides die.
    """

    def test_goal_above_max(self):

        chance = roll_success_range(0, 5, 6, above=True, equal=True)

        self.assertEqual(None, chance)

    def test_goal_0(self):

        chance = roll_success_range(0, 5, 0, above=True, equal=True)

        self.assertEqual({"min": 0, "max": 5}, chance)

    def test_goal_1(self):

        chance = roll_success_range(0, 5, 1, above=True, equal=True)

        self.assertEqual({"min": 1, "max": 5}, chance)

    def test_goal_2(self):

        chance = roll_success_range(0, 5, 2, above=True, equal=True)

        self.assertEqual({"min": 2, "max": 5}, chance)

    def test_goal_3(self):

        chance = roll_success_range(0, 5, 3, above=True, equal=True)

        self.assertEqual({"min": 3, "max": 5}, chance)

    def test_goal_4(self):

        chance = roll_success_range(0, 5, 4, above=True, equal=True)

        self.assertEqual({"min": 4, "max": 5}, chance)

    def test_goal_5(self):

        chance = roll_success_range(0, 5, 5, above=True, equal=True)

        self.assertEqual({"min": 5, "max": 5}, chance)

