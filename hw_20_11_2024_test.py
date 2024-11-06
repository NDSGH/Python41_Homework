# Протестируем функции из файла hw_20_11_2024

import unittest
import hw_20_11_2024


class TestSet(unittest.TestCase):
    def test_bare_1(self):
        """Equal None test fun 1"""
        result = hw_20_11_2024.set_fun_1([])
        self.assertEqual(result, None)

    def test_bare_2(self):
        """Equal None test fun 2"""
        result = hw_20_11_2024.set_fun_2([])
        self.assertEqual(result, None)

    def test_list_1(self):
        """Equal test fun 1"""
        result = hw_20_11_2024.set_fun_1([-5, -5, 0])
        self.assertEqual(result, [-5, 0])

    def test_list_2(self):
        """Equal test fun 2"""
        result = hw_20_11_2024.set_fun_1([-5, -5, 0])
        self.assertEqual(result, [-5, 0])


if __name__ == '__main__':
    unittest.main()
