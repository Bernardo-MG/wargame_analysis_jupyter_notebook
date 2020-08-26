# -*- coding: utf-8 -*-

import unittest
from decimal import Decimal

from scripts.probability import success_chance

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
        chance = success_chance(0, 0, 0, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_min(self):

        chance = success_chance(1, 1, 1, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_zero_goal(self):

        chance = success_chance(1, 1, 0, above=True, equal=False)

        self.assertEqual(1, chance)


class TestMinValuesAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
    """

    def test_zeros(self):

        chance = success_chance(0, 0, 0, above=True, equal=True)

        self.assertEqual(1, chance)

    def test_min(self):

        chance = success_chance(1, 1, 1, above=True, equal=True)

        self.assertEqual(1, chance)

    def test_zero_goal(self):

        chance = success_chance(1, 1, 0, above=True, equal=True)

        self.assertEqual(1, chance)


class TestMinValuesBelow(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
    """

    def test_zeros(self):
        chance = success_chance(0, 0, 0, above=False, equal=False)

        self.assertEqual(0, chance)

    def test_min(self):

        chance = success_chance(1, 1, 1, above=False, equal=False)

        self.assertEqual(0, chance)

    def test_zero_goal(self):

        chance = success_chance(1, 1, 0, above=False, equal=False)

        self.assertEqual(0, chance)


class TestMinValuesBelowEqual(unittest.TestCase):
    """
    Tests the chance to go above with minimal values.
    """

    def test_zeros(self):
        chance = success_chance(0, 0, 0, above=False, equal=True)

        self.assertEqual(Decimal('1'), chance)

    def test_min(self):

        chance = success_chance(1, 1, 1, above=False, equal=True)

        self.assertEqual(Decimal('1'), chance)

    def test_zero_goal(self):

        chance = success_chance(1, 1, 0, above=False, equal=True)

        self.assertEqual(0, chance)


class TestNegValuesAbove(unittest.TestCase):
    """
    Tests the chance to go above with negative values values.
    """

    def test_negs(self):

        chance = success_chance(-1, -1, -1, above=True, equal=False)

        self.assertEqual(0, chance)

    def test_neg_goal(self):

        chance = success_chance(1, 10, -1, above=True, equal=False)

        self.assertEqual(1, chance)


class TestNegValuesAboveEqual(unittest.TestCase):
    """
    Tests the chance to go above with negative values values.
    """

    def test_negs(self):

        chance = success_chance(-1, -1, -1, above=True, equal=True)

        self.assertEqual(Decimal('1'), chance)

    def test_neg_goal(self):

        chance = success_chance(1, 10, -1, above=True, equal=True)

        self.assertEqual(1, chance)


class TestNegValuesBelow(unittest.TestCase):
    """
    Tests the chance to go above with negative values values.
    """

    def test_negs(self):

        chance = success_chance(-1, -1, -1, above=False, equal=False)

        self.assertEqual(0, chance)

    def test_neg_goal(self):

        chance = success_chance(1, 10, -1, above=False, equal=False)

        self.assertEqual(0, chance)


class TestNegValuesBelowEqual(unittest.TestCase):
    """
    Tests the chance to go above with negative values values.
    """

    def test_negs(self):

        chance = success_chance(-1, -1, -1, above=False, equal=True)

        self.assertEqual(Decimal('1'), chance)

    def test_neg_goal(self):

        chance = success_chance(1, 10, -1, above=False, equal=True)

        self.assertEqual(0, chance)
