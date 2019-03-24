import unittest
from compare_versions import compare_versions
from .test_cases import valid_test_cases, invalid_test_cases


class TestCompareVersions(unittest.TestCase):
    def test_invalid_input(self):
    	for versions, expected in invalid_test_cases:
    		with self.subTest():
    			with self.assertRaises(ValueError):
    				compare_versions(versions[0], versions[1])

    def test_valid_input(self):
    	for versions, expected in valid_test_cases:
            with self.subTest():
                self.assertEqual(compare_versions(versions[0], versions[1]), expected)


if __name__ == '__main__':
    unittest.main()