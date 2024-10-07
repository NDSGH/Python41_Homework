# Протестируем функцию проверки числа на простое/не простое

import unittest

import hw_21_10_2024


class TestIsPrime(unittest.TestCase):
    def test_arg_nan(self):
        """NaN test"""
        result = hw_21_10_2024.is_prime('some string')
        self.assertEqual(result, None)

    def test_arg_true(self):
        """True test"""
        result = hw_21_10_2024.is_prime(17)
        self.assertTrue(result)

    def test_arg_false(self):
        """False test"""
        result = hw_21_10_2024.is_prime(0)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
