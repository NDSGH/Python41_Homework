# Протестируем основную функцию

import unittest
import hw_23_12_2024


class TestFilter(unittest.TestCase):
    def test_str(self):
        """simple equal test"""
        result = hw_23_12_2024.filtr(hw_23_12_2024.f, [0, 1, -1])
        self.assertEqual(result, [0, 1])


if __name__ == '__main__':
    unittest.main()
