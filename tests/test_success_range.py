# -*- coding: utf-8 -*-

import unittest

from scripts.probability import roll_success_range

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestMinValuesAbove(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
    """

    def test_zeros(self):
        chance = roll_success_range(0, 0, 0, above=True, equal=False)

        self.assertEqual(None, chance)

    def test_min(self):

        chance = roll_success_range(1, 1, 1, above=True, equal=False)

        self.assertEqual(None, chance)

    def test_zero_goal(self):

        chance = roll_success_range(1, 1, 0, above=True, equal=False)

        self.assertEqual({"min": 1, "max": 1}, chance)


class TestMinValuesAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
    """

    def test_zeros(self):

        chance = roll_success_range(0, 0, 0, above=True, equal=True)

        self.assertEqual({"min": 0, "max": 0}, chance)

    def test_min(self):

        chance = roll_success_range(1, 1, 1, above=True, equal=True)

        self.assertEqual({"min": 1, "max": 1}, chance)

    def test_zero_goal(self):

        chance = roll_success_range(1, 1, 0, above=True, equal=True)

        self.assertEqual({"min": 1, "max": 1}, chance)


class TestMinValuesBelow(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
    """

    def test_zeros(self):
        chance = roll_success_range(0, 0, 0, above=False, equal=False)

        self.assertEqual(None, chance)

    def test_min(self):

        chance = roll_success_range(1, 1, 1, above=False, equal=False)

        self.assertEqual(None, chance)

    def test_zero_goal(self):

        chance = roll_success_range(1, 1, 0, above=False, equal=False)

        self.assertEqual(None, chance)


class TestMinValuesBelowEqual(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
    """

    def test_zeros(self):
        chance = roll_success_range(0, 0, 0, above=False, equal=True)

        self.assertEqual({"min": 0, "max": 0}, chance)

    def test_min(self):

        chance = roll_success_range(1, 1, 1, above=False, equal=True)

        self.assertEqual({"min": 1, "max": 1}, chance)

    def test_zero_goal(self):

        chance = roll_success_range(1, 1, 0, above=False, equal=True)

        self.assertEqual(None, chance)


class TestNegValuesAbove(unittest.TestCase):
    """
    Tests the chance to go above with negative values values.
    """

    def test_negs(self):

        chance = roll_success_range(-1, -1, -1, above=True, equal=False)

        self.assertEqual(None, chance)

    def test_neg_goal(self):

        chance = roll_success_range(1, 10, -1, above=True, equal=False)

        self.assertEqual({"min": 1, "max": 10}, chance)


class TestNegValuesAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with negative values values.
    """

    def test_negs(self):

        chance = roll_success_range(-1, -1, -1, above=True, equal=True)

        self.assertEqual({"min": -1, "max": -1}, chance)

    def test_neg_goal(self):

        chance = roll_success_range(1, 10, -1, above=True, equal=True)

        self.assertEqual({"min": 1, "max": 10}, chance)


class TestNegValuesBelow(unittest.TestCase):
    """
    Tests the chance to go above with negative values values.
    """

    def test_negs(self):

        chance = roll_success_range(-1, -1, -1, above=False, equal=False)

        self.assertEqual(None, chance)

    def test_neg_goal(self):

        chance = roll_success_range(1, 10, -1, above=False, equal=False)

        self.assertEqual(None, chance)


class TestNegValuesBelowEqual(unittest.TestCase):
    """
    Tests the chance to go above with negative values values.
    """

    def test_negs(self):

        chance = roll_success_range(-1, -1, -1, above=False, equal=True)

        self.assertEqual({"min": -1, "max": -1}, chance)

    def test_neg_goal(self):

        chance = roll_success_range(1, 10, -1, above=False, equal=True)

        self.assertEqual(None, chance)
