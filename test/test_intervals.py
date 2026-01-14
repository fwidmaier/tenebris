import unittest
from tenebris.sets.interval import Interval


class TestIntervals(unittest.TestCase):
    def test1(self):
        i = Interval(0, 1)
        self.assertTrue(0 in i)
        self.assertTrue(1 in i)
        self.assertFalse(2 in i)

    def testCrossProduct(self):
        i = Interval(0, 1)
        j = Interval(0, 1)
        self.assertTrue((0, 1) in i.times(j))
