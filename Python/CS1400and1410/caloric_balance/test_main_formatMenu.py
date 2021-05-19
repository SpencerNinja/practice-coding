"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest

import main


class TestFormatMenu(unittest.TestCase):
    def test001_formatMenuExists(self):
        self.assertTrue('formatMenu' in dir(main),
                        'Function "formatMenu" is not defined, check your spelling')
        return

    def test002_formatMenuContainsAllActions(self):
        from main import formatMenu
        actual = formatMenu()
        self.assertTrue(type(actual) is list, 'formatMenu did not return a list')

        expected = [
            "[f]",
            "[a]",
            "[q]"
        ]
        for expected_line in expected:
            found = False
            for actual_line in actual:
                if expected_line in actual_line.lower():
                    found = True
                    break
            self.assertTrue(found, "'" + expected_line + "' not found in formatMenu return")


if __name__ == '__main__':
    unittest.main()
