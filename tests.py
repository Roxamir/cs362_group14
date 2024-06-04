import unittest
import task
import random


class TestCases(unittest.TestCase):
    # test conv_num
    # function 1
    def test_conv_num_neg(self):
        self.assertEqual(task.conv_num('-42352'), -42352)

    def test_conv_num_neg_hexa(self):
        self.assertEqual(task.conv_num('-0x3A2'), -930)

    def test_conv_num_hexa_mixed_case(self):
        self.assertEqual(task.conv_num('0Xaf53BC'), 11490236)

    def test_conv_num_hexa_with_decimal(self):
        self.assertEqual(task.conv_num('0xA3F.12'), None)

    def test_conv_num_decimal_end(self):
        self.assertEqual(task.conv_num('12345.'), 12345.0)

    def test_conv_num_decimal_start(self):
        self.assertEqual(task.conv_num('.12345'), 0.12345)

    def test_conv_num_int_with_letter(self):
        self.assertEqual(task.conv_num('7123DA'), None)

    def test_conv_num_wrong_hex_letter(self):
        self.assertEqual(task.conv_num('0x123X'), None)

    def test_conv_num_empty_hex(self):
        self.assertEqual(task.conv_num('0x'), None)

    def test_conv_num_multiple_decimals(self):
        self.assertEqual(task.conv_num('1.23.45'), None)


if __name__ == '__main__':
    unittest.main()
