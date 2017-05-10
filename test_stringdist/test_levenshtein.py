# Copyright (c) 2017 Oleg Bulkin
# MIT License (https://opensource.org/licenses/MIT)

# Import methods being tested and base class provided by unittest
from stringdist import levenshtein, levenshtein_norm
from unittest import TestCase


# Create Levenshetin test case using unittest base class. Each method
# represents a unit test, with success criteria described via docstring
class TestLevenshtein(TestCase):

    def test_levenshtein_matching(self):
        """It should return correct distance when strings match"""
        self.assertEqual(levenshtein('abcde', 'abcde'), 0)

    def test_levenshtein_deletion(self):
        """It should return correct distance when deletion is involved"""
        self.assertEqual(levenshtein('abcd!', 'abcd'), 1)

    def test_levenshtein_insertion(self):
        """It should return correct distance when insertion is involved"""
        self.assertEqual(levenshtein('abcd', 'abcde'), 1)

    def test_levenshtein_substitution(self):
        """It should return correct distance when substitution is involved"""
        self.assertEqual(levenshtein('abcd!', 'abcde'), 1)

    def test_levenshtein_norm_matching(self):
        """It should return right normalized dist when strings match"""
        self.assertEqual(levenshtein_norm('abcde', 'abcde'), 0)

    def test_levenshtein_norm_deletion(self):
        """It should return right normalized dist when deletion involved"""
        self.assertEqual(levenshtein_norm('abcd!', 'abcd'), 0.2)

    def test_levenshtein_norm_insertion(self):
        """It should return right normalized dist when insertion involved"""
        self.assertEqual(levenshtein_norm('abcd', 'abcde'), 0.2)

    def test_levenshtein_norm_substitution(self):
        """It should return right normalized dist when substitution involved"""
        self.assertEqual(levenshtein_norm('abcd!', 'abcde'), 0.2)
