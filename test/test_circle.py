import unittest
import math
import circle

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0.0)

    def test_area_standard(self):
        res = circle.area(2)
        # Сравниваем с точностью до 5 знаков после запятой
        self.assertAlmostEqual(res, 12.56637, places=5) 

    def test_perimeter_standard(self):
        res = circle.perimeter(2)
        self.assertAlmostEqual(res, 12.56637, places=5)

if __name__ == '__main__':
    unittest.main()