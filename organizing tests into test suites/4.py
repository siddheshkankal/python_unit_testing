import unittest
from test_animals import TestCats, TestDogs
 
 
suite = unittest.TestSuite()
 
suite.addTest(unittest.makeSuite(TestCats))
suite.addTest(unittest.makeSuite(TestDogs))
 
runner = unittest.TextTestRunner()
runner.run(suite)
