#!/usr/bin/python3
import unittest
import FunRead

class TestCalc(unittest.TestCase):

    def test_myread(self):
        self.assertEqual(FunRead.fun_read('README.txt'),'My Read file\n')


if __name__ == '__main__':
    unittest.main()
