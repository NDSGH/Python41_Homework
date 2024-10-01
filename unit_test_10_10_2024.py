# Протестируем функции из файла hw_10_10_2024 на работу с пустым списком, символьным списком и строкой

import unittest
import hw_10_10_2024


class TestTwoMax(unittest.TestCase):
    def test_empty_1(self):
        """Empty list test"""
        empty = []
        res = hw_10_10_2024.two_of_max_1(empty)
        self.assertEqual(res, [])

    def test_empty_2(self):
        """Empty list test"""
        empty = []
        res = hw_10_10_2024.two_of_max_2(empty)
        self.assertEqual(res, [])

    def test_nan_1(self):
        """NaN test"""
        some_list = ['a', 'b', 'c']
        res = hw_10_10_2024.two_of_max_1(some_list)
        self.assertEqual(res, ['c', 'b'])

    def test_nan_2(self):
        """NaN test"""
        some_list = ['a', 'b', 'c']
        res = hw_10_10_2024.two_of_max_2(some_list)
        self.assertEqual(res, ['c', 'b'])


if __name__ == '__main__':
    unittest.main()
