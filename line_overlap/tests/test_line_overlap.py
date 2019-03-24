import unittest
from line_overlap import check_overlap
from .test_cases import valid_test_cases, invalid_test_cases


class TestLineOverLap(unittest.TestCase):
    def test_invalid_input(self):
    	for points, expected in invalid_test_cases:
    		with self.subTest():
    			with self.assertRaises(TypeError):
    				check_overlap(points[0], points[1])

    def test_valid_input(self):
    	for points, expected in valid_test_cases:
    		with self.subTest():
    			self.assertEqual(check_overlap(points[0], points[1]), expected)


if __name__ == '__main__':
    unittest.main()