# Протестируем функции из файла hw_03_10_2024 на приём в качестве аргумента пустой строки (возвр. None)

import unittest
import hw_03_10_2024


class TestReverseFun(unittest.TestCase):
    def test_empty_1(self):
        empty = ''
        res = hw_03_10_2024.reverser_fun_1(empty)
        self.assertEqual(res, None)

    def test_empty_2(self):
        empty = ''
        res = hw_03_10_2024.reverser_fun_2(empty)
        self.assertEqual(res, None)

    def test_empty_3(self):
        empty = ''
        res = hw_03_10_2024.reverser_fun_3(empty)
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
