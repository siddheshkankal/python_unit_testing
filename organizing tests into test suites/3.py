import unittest
from test_arithmetic import TestAdditionAndSubtraction
from test_arithmetic import TestMultiplicationAndDivision
 
 
suite = unittest.TestSuite()
 
suite.addTest(unittest.makeSuite(TestAdditionAndSubtraction))
suite.addTest(unittest.makeSuite(TestMultiplicationAndDivision))
 
runner = unittest.TextTestRunner()
runner.run(suite)
