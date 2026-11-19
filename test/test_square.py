import unittest
import square

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_standard(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_perimeter_standard(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

if __name__ == '__main__':
    unittest.main()