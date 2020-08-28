# -*- coding: utf-8 -*-

import unittest

from scripts.probability import at_least_one

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestMinValues(unittest.TestCase):
    """
    Tests the chance of at least one with minimal values.
    """

    def test_zeros(self):
        chance = at_least_one(0, 0)

        self.assertEqual(0, chance)

    def test_min(self):
        chance = at_least_one(1, 1)

        self.assertEqual(1, chance)

    def test_no_chance(self):
        chance = at_least_one(0, 1)

        self.assertEqual(0, chance)

    def test_no_attempts(self):
        chance = at_least_one(1, 0)

        self.assertEqual(0, chance)


class TestInvalidChance(unittest.TestCase):
    """
    Tests with an invalid chance.
    """

    def test_zeros(self):
        chance = at_least_one(2, 1)

        self.assertEqual(1, chance)


class TestSingleAttempt(unittest.TestCase):
    """
    Tests the chance of at least one with minimal values.
    """

    def test_10percent(self):
        chance = at_least_one(0.1, 1)

        self.assertEqual(0.09999999999999998, chance)

    def test_50percent(self):
        chance = at_least_one(0.5, 1)

        self.assertEqual(0.5, chance)

    def test_60percent(self):
        chance = at_least_one(0.6, 1)

        self.assertEqual(0.6, chance)

    def test_100percent(self):
        chance = at_least_one(1, 1)

        self.assertEqual(1, chance)


class TestThreeAttempt(unittest.TestCase):
    """
    Tests the chance of at least one with minimal values.
    """

    def test_10percent(self):
        chance = at_least_one(0.1, 3)

        self.assertEqual(0.2709999999999999, chance)

    def test_50percent(self):
        chance = at_least_one(0.5, 3)

        self.assertEqual(0.875, chance)

    def test_100percent(self):
        chance = at_least_one(1, 3)

        self.assertEqual(1, chance)
