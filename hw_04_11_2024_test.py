# Протестируем созданные функции

import unittest

import hw_04_11_2024


class TestIntToBin(unittest.TestCase):
    def test_negative_1(self):
        """Simple equal test fun 1"""
        result = hw_04_11_2024.int_to_bin_1(-15)
        self.assertEqual(result, '-1111')

    def test_negative_2(self):
        """Simple equal test fun 2"""
        result = hw_04_11_2024.int_to_bin_2(-15)
        self.assertEqual(result, '-1111')

    def test_type_1(self):
        """Type checking fun 1"""
        result = hw_04_11_2024.int_to_bin_1(0)
        self.assertTrue(isinstance(result, str))

    def test_type_2(self):
        """Type checking fun 2"""
        result = hw_04_11_2024.int_to_bin_2(0)
        self.assertTrue(isinstance(result, str))
