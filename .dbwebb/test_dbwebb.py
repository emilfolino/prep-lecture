#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import unittest
from unittest.mock import patch
from importlib import util
from io import StringIO
from modulefinder import ModuleFinder
import os
import sys

proj_path = os.path.realpath(sys.argv.pop())
if proj_path not in sys.path:
    sys.path.insert(0, proj_path)
#pylint: disable=wrong-import-position
import exam
#pylint: enable=wrong-import-position



class TestFunc(unittest.TestCase):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """


    def test_a_module(self):
        """
        Test that module and functions exist
        """
        self.assertIsNotNone(util.find_spec("exam"))
        self.assertTrue(hasattr(exam, "validate_email"))
        self.assertTrue(hasattr(exam, "verify_hex"))
        self.assertTrue(hasattr(exam, "find_duplicates"))
        self.assertTrue(hasattr(exam, "analyze_text"))
        self.assertTrue(hasattr(exam, "types"))

    def test_b_analyze_text(self):
        """
        Test assignment 1
        """
        self.assertNotEqual(exam.analyze_text.__doc__.strip(), "Assignment 1")
        self.assertIsNotNone(util.find_spec("analyze_functions"))
        inp = ["s", "g", "Gobble gobble", "q"]
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                code = exam.analyze_text()
                str_data = fake_out.getvalue().strip("\n")
                list_data = str_data.split("\n")
                self.assertEqual(list_data, ['6', '5', '5', '21', '8', '1', 'Not an option!'])
                self.assertTrue(code)

    def test_c_verify_hex(self):
        """
        Test assignment 2
        """
        self.assertNotEqual(exam.verify_hex.__doc__.strip(), "Assignment 2")

        match = ["#fff", "#000", "#fc6c85", "#6495ed"]
        not_match = ["fff", "#ffff", "#fffffff", "fff#", "#FFFFFF"]

        for case in match:
            self.assertTrue(exam.verify_hex(case))

        for case in not_match:
            self.assertFalse(exam.verify_hex(case))

    def test_d_find_duplicates(self):
        """
        Test assignment 3
        """
        self.assertNotEqual(exam.find_duplicates.__doc__.strip(), "Assignment 3")
        empty = []
        self.assertEqual(exam.find_duplicates(empty), [])
        no_dups = ["hej", "hopp"]
        self.assertEqual(exam.find_duplicates(no_dups), [])
        dups = ["hej", "hopp", "hej"]
        self.assertEqual(exam.find_duplicates(dups), ["hej"])
        mult_dups = ["oj", "hej", "oj", "hopp", "hej"]
        self.assertEqual(exam.find_duplicates(mult_dups), ["hej", "oj"])
        upper = ["hej", "Hej"]
        self.assertEqual(exam.find_duplicates(upper), ["hej"])

    def test_e_types(self):
        """
        Test assignment 4
        """
        self.assertNotEqual(exam.types.__doc__.strip(), "Assignment 4")
        base = [1, "hej", ["3", "4", "5"]]
        self.assertEqual(exam.types(base), "The square of 1 is 1. The secret word is hej. The list contains 3, 4, 5.")
        single = [12]
        self.assertEqual(exam.types(single), "The square of 12 is 144.")
        sqr = [2, 5, 8]
        self.assertEqual(exam.types(sqr), "The square of 2 is 4. The square of 5 is 25. The square of 8 is 64.")
        # sqr_dict = [2, {"hej": "dig"}]
        # self.assertEqual(exam.types(sqr_dict), "The square of 2 is 4.")
        mult_list = [1, "hej", ["3", "4", "5", "hej", "haha"]]
        self.assertEqual(exam.types(mult_list),
                         "The square of 1 is 1. The secret word is hej. The list contains 3, 4, 5, hej, haha.")
        empty = []
        self.assertEqual(exam.types(empty), "")

    def test_f_validate_email(self):
        """
        Test assignment 5
        """
        self.assertNotEqual(exam.validate_email.__doc__.strip(), "Assignment 5")

        match = ["abc@dbwebb.com", ".@dbwebb.com", "ab_c@dbwebb.com", "ab-c@dbwebb.com",
                 "aa.b-c@dbwebb.com", "aa.b-c@dbw.ebb.com", "a23c@dbwebb.com", "abc@dbwebb.co3", "abc@dbwebb.se"]
        not_match = ["abcdbwebb.com", "@dbwebb.com", "abc@asf..com", "abc@.com",
                     "ab c@dbwebb.com",
                     "ab:c@dbwebb.com", "ab!c@dbwebb.com", "aåc@dbwebb.com",
                     "abcdbwebb.c", "ab-c@dbwebbcom", "aa.b-c@dbwebb.coms",
                     "Awac@dbwebb.com", "aa.b-c@dbwebb.coms", "aa.b-c@db@webb.com"]

        for case in match:
            self.assertTrue(exam.validate_email(case))

        for case in not_match:
            self.assertFalse(exam.validate_email(case))

if __name__ == '__main__':
    unittest.main(verbosity=2)
