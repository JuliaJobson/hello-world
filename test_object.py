#!/usr/bin/python3
import unittest
import ObjectTesting

class TestCalc(unittest.TestCase):

    def test_recipeobject_ingredient(self):
        myrecipe = ObjectTesting.Recipe(['Salad'], [2])
        result = myrecipe.catch_ingredient()
        self.assertEqual( ['Salad'] ,result)

    def test_recipeobject_time(self):
        myrecipe = ObjectTesting.Recipe(['Salad'], [1])


if __name__ == '__main__':
    unittest.main()
