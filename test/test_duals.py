import unittest
from tenebris import Dual


class Test(unittest.TestCase):
    def test_add1(self):
        d1 = Dual(1, 2)
        d2 = Dual(2, 2)
        res = d1 + d2
        self.assertEqual(res.a, 3)
        self.assertEqual(res.b, 4)

    def test_add2(self):
        d1 = Dual(1, 2)
        res = 1 + d1 + 2
        self.assertEqual(res.a, 4)
        self.assertEqual(res.b, 2)

    def test_sub1(self):
        d1 = Dual(1, 2)
        d2 = Dual(2, 2)
        res = d1 - d2
        self.assertEqual(res.a, -1)
        self.assertEqual(res.b, 0)

    def test_sub2(self):
        d1 = Dual(1, 2)
        res = 1 - d1 + 2
        self.assertEqual(res.a, 2)
        self.assertEqual(res.b, -2)

    def test_mul1(self):
        d1 = Dual(1, 2)
        d2 = Dual(2, 2)
        res = d1 * d2
        self.assertEqual(res.a, 2)
        self.assertEqual(res.b, 6)

    def test_mul2(self):
        d1 = Dual(1, 2)
        res = 3 * d1 * 2
        self.assertEqual(res.a, 6)
        self.assertEqual(res.b, 12)

    def test_div1(self):
        d1 = Dual(1, 2)
        d2 = Dual(2, 2)
        res = d1 / d2
        self.assertEqual(res.a, 0.5)
        self.assertEqual(res.b, 0.5)

    def test_div2(self):
        d1 = Dual(1, 2)
        res1 = d1 / 2
        self.assertEqual(res1.a, 0.5)
        self.assertEqual(res1.b, 1)
        res2 = 1 / d1
        self.assertEqual(res2.a, 1)
        self.assertEqual(res2.b, -2)


if __name__ == '__main__':
    unittest.main()
