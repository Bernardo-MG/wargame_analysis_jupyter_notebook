# -*- coding: utf-8 -*-

import unittest
import math

from scripts.action import max_actions

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestMinValues(unittest.TestCase):
    """
    Tests the max actions with minimal values.
    """

    def test_zeros(self):
        actions = max_actions(0, 0, 0, 0)

        self.assertEqual(0, actions)

    def test_min(self):
        actions = max_actions(1, 1, 1, 1)

        self.assertEqual(1, actions)

    def test_no_max(self):
        actions = max_actions(1, 1, 1, 0)

        self.assertEqual(0, actions)


class TestPercentile(unittest.TestCase):
    """
    Tests the max actions with percentile values.
    """

    def test_full_turn(self):
        actions = max_actions(100, 100, 15, 3)

        self.assertEqual(1, actions)

    def test_half_turn_enough_ammo(self):
        actions = max_actions(100, 50, 15, 2)

        self.assertEqual(2, actions)

    def test_half_turn_no_recovery_needed_high_limit(self):
        actions = max_actions(100, 50, 15, 3)

        self.assertEqual(2, actions)

    def test_half_turn_no_recovery_needed_exact_limit(self):
        actions = max_actions(100, 50, 15, 2)

        self.assertEqual(2, actions)

    def test_half_turn_recovery_needed(self):
        actions = max_actions(100, 50, 15, 1)

        self.assertEqual(1, actions)


class TestPercentileUnlimited(unittest.TestCase):
    """
    Tests the max actions with percentile values and unlimited actions.
    """

    def test_full_turn(self):
        actions = max_actions(100, 100, 15, math.inf)

        self.assertEqual(1, actions)

    def test_half_turn(self):
        actions = max_actions(100, 50, 15, math.inf)

        self.assertEqual(2, actions)
