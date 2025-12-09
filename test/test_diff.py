import unittest
from tenebris import d


class Test(unittest.TestCase):
    def test_diff(self):
        f = lambda x: 1
        df = d(f)
        self.assertEqual(df(9), 0)

    def test_diff2(self):
        df = d(lambda x: x * x)
        diffs = [df(i) for i in range(10)]
        self.assertEqual(diffs, [2 * i for i in range(10)])

    def test_diff3(self):
        df = d(lambda x: 1 / x)
        self.assertEqual(df(1), -1)


if __name__ == '__main__':
    unittest.main()

