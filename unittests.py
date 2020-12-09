import unittest

from Unittests.Utest_Pet.test_Pet_Module import *
from Unittests.Utest_Pet.test_Cat_Module import *
from Unittests.Utest_Livestocks.test_Livestock_Module import *
from Unittests.Utest_Livestocks.test_Cow_Module import *

"""
This file will be used for creating test suits

"""


def Animal_testsuite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(test_livestock))
    suite.addTest(unittest.makeSuite(test_livestock))

    suite.addTest(unittest.makeSuite(test_Pet))
    suite.addTest(unittest.makeSuite(test_Cat))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))


if __name__ == "__main__":
    Animal_testsuite()
