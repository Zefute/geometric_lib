import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_standard(self):
        res = rectangle.area(3, 4)
        self.assertEqual(res, 12)

    def test_perimeter_standard(self):
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14)
        
    def test_area_float(self):
        res = rectangle.area(2.5, 4.0)
        self.assertEqual(res, 10.0)

if __name__ == '__main__':
    unittest.main()