# Copyright (c) 2017 Oleg Bulkin
# MIT License (https://opensource.org/licenses/MIT)

# Bring unit test classes up into test module namespace so that the module can
# be passed directly to unittest when testing from the command line
from .test_levenshtein import TestLevenshtein
from .test_rdlevenshtein import TestRdlevenshtein
