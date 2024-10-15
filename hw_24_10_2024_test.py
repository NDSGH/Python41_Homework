# Простой тест для двух функций из файла hw_24_10_2024

import unittest
import hw_24_10_2024


class TestSorting(unittest.TestCase):
    def test_sort_empty(self):
        """Test empty list"""
        result = hw_24_10_2024.bubble_sort([])
        self.assertEqual(result, [])

    def test_sort_empty_2(self):
        """Test empty list"""
        result = hw_24_10_2024.inbuilt_sort([])
        self.assertEqual(result, [])

    def test_sort_true(self):
        """Test list"""
        result = hw_24_10_2024.bubble_sort([0, -2, 36])
        self.assertEqual(result, [-2, 0, 36])

    def test_sort_true_2(self):
        """Test list"""
        result = hw_24_10_2024.inbuilt_sort([0, -2, 36])
        self.assertEqual(result, [-2, 0, 36])


if __name__ == '__main__':
    unittest.main()
