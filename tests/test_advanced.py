# -*- coding: utf-8 -*-

from .context import analysis

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        assert True


if __name__ == '__main__':
    unittest.main()
