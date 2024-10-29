# Simple unit test for functions in hw_11_11_2024

import unittest
import hw_11_11_2024

class TestMaxRep(unittest.TestCase):
    def test_empty_1(self):
        """Empty list test"""
        empty_in = []
        res = hw_11_11_2024.friq_num_1(empty_in)
        self.assertEqual(res, None)

    def test_empty_2(self):
        """Empty list test"""
        empty_in = []
        res = hw_11_11_2024.friq_num_2(empty_in)
        self.assertEqual(res, None)

    def test_res_1(self):
        """Num list test"""
        not_empty_in = [4, 4, 4, 0, 1]
        res = hw_11_11_2024.friq_num_1(not_empty_in)
        self.assertEqual(res, [4])

    def test_res_2(self):
        """Num list test"""
        not_empty_in = [4, 4, 4, 0, 1]
        res = hw_11_11_2024.friq_num_2(not_empty_in)
        self.assertEqual(res, [4])


if __name__ == '__main__':
    unittest.main()
