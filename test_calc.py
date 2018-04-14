#!/usr/bin/python3
import unittest
import calc
#To test the code use python3 -m unittest testReading.py

class TestCalc(unittest.TestCase):

    def test_add(self): #must start with test_ to work
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_add_fail(self): #must start with test_ to work
        result = calc.add(10, 5)
        self.assertEqual(result, 10)

#to be able to use python3 test_calc.py

if __name__ == '__main__':
    unittest.main()
