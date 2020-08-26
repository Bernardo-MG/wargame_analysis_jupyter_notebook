# -*- coding: utf-8 -*-

import unittest
import math

from scripts.action import hits_to_kill

"""
Max shots script tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestMinValues(unittest.TestCase):
    """
    Tests the hits of at least one with minimal values.
    """

    def test_zeros(self):
        hits = hits_to_kill(0, 0)

        self.assertEqual(0, hits)

    def test_min(self):
        hits = hits_to_kill(1, 1)

        self.assertEqual(1, hits)

    def test_no_damage(self):
        hits = hits_to_kill(0, 1)

        self.assertEqual(math.inf, hits)

    def test_no_health(self):
        hits = hits_to_kill(1, 0)

        self.assertEqual(0, hits)


class TestCommon(unittest.TestCase):
    """
    Tests the hits of at least one with minimal values.
    """

    def test_tenth(self):
        hits = hits_to_kill(1, 10)

        self.assertEqual(10, hits)

    def test_half(self):
        hits = hits_to_kill(5, 10)

        self.assertEqual(2, hits)

    def test_equal(self):
        hits = hits_to_kill(10, 10)

        self.assertEqual(1, hits)
