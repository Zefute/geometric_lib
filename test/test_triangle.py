import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0.0)

    def test_area_standard(self):
        res = triangle.area(6, 4)
        self.assertEqual(res, 12.0)

    def test_perimeter_standard(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

if __name__ == '__main__':
    unittest.main()