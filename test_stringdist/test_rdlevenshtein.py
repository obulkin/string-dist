# Copyright (c) 2017 Oleg Bulkin
# MIT License (https://opensource.org/licenses/MIT)

# Import methods being tested and base class provided by unittest
from stringdist import rdlevenshtein, rdlevenshtein_norm
from unittest import TestCase


# Create restricted Damerau-Levenshetein (a.k.a. optimal string alignment
# distance) test case using unittest base class. Each method in the class
# represents a unit test, with success criteria described via docstring
class TestRdlevenshtein(TestCase):

    def test_rdlevenshtein_matching(self):
        """It should return correct distance when strings match"""
        self.assertEqual(rdlevenshtein('abcde', 'abcde'), 0)

    def test_rdlevenshtein_deletion(self):
        """It should return correct distance when deletion is involved"""
        self.assertEqual(rdlevenshtein('abcd!', 'abcd'), 1)

    def test_rdlevenshtein_insertion(self):
        """It should return correct distance when insertion is involved"""
        self.assertEqual(rdlevenshtein('abcd', 'abcde'), 1)

    def test_rdlevenshtein_substitution(self):
        """It should return correct distance when substitution is involved"""
        self.assertEqual(rdlevenshtein('abcd!', 'abcde'), 1)

    def test_rdlevenshtein_transposition(self):
        """It should return correct distance when transposition is involved"""
        self.assertEqual(rdlevenshtein('abced', 'abcde'), 1)

    def test_rdlevenshtein_norm_matching(self):
        """It should return right normalized dist when strings match"""
        self.assertEqual(rdlevenshtein_norm('abcde', 'abcde'), 0)

    def test_rdlevenshtein_norm_deletion(self):
        """It should return right normalized dist when deletion involved"""
        self.assertEqual(rdlevenshtein_norm('abcd!', 'abcd'), 0.2)

    def test_rdlevenshtein_norm_insertion(self):
        """It should return right normalized dist when insertion involved"""
        self.assertEqual(rdlevenshtein_norm('abcd', 'abcde'), 0.2)

    def test_rdlevenshtein_norm_substitution(self):
        """It should return right normalized dist when substitution involved"""
        self.assertEqual(rdlevenshtein_norm('abcd!', 'abcde'), 0.2)

    def test_rdlevenshtein_norm_transposition(self):
        """It should return right normalized dist when transposing involved"""
        self.assertEqual(rdlevenshtein_norm('abced', 'abcde'), 0.2)
