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

    def test_conv_num_zero_hexa(self):
        self.assertEqual(task.conv_num('0x0'), 0)

    def tes_conv_num_zero_decimal(self):
        self.assertEqual(task.conv_num('0'), 0)

    # test my_datetime
    # function 2
    def test_epoch_start(self):
        self.assertEqual(task.my_datetime(0), '01-01-1970')

    def test_non_leap_year(self):
        # January 2, 1970
        self.assertEqual(task.my_datetime(86400), '01-02-1970')
        # December 31, 1970
        self.assertEqual(task.my_datetime(31536000 - 86400), '12-31-1970')

    def test_leap_year(self):
        # January 1, 1972
        self.assertEqual(task.my_datetime(63072000), '01-01-1972')
        # March 1, 1972 (68256000 seconds calculated previously)
        self.assertEqual(task.my_datetime(68256000), '03-01-1972')

    def test_boundary_conditions(self):
        # December 31, 1971
        self.assertEqual(task.my_datetime(63072000 - 86400), '12-31-1971')
        # January 1, 1973
        self.assertEqual(task.my_datetime(94608000), '12-31-1972')

    def test_large_number_of_seconds(self):
        # January 1, 2000
        self.assertEqual(task.my_datetime(946684800), '01-01-2000')
        # January 1, 2020
        self.assertEqual(task.my_datetime(1577836800), '01-01-2020')

    def test_known_dates(self):
        # July 20, 1969, in seconds since epoch would be negative (before 1970), so we'll skip this test
        # Some other known dates
        self.assertEqual(task.my_datetime(1234567890), '02-13-2009')
        self.assertEqual(task.my_datetime(1500000000), '07-14-2017')

    # test conv_endian
    # function 3
    def test_conv_endian_little_pos(self):
        """Tests conv_endian function for positive little endian."""
        self.assertEqual('32 6B', task.conv_endian(27442, 'little'))

    def test_conv_endian_big_pos(self):
        """Tests conv_endian function for positive big endian."""
        self.assertEqual('16 61', task.conv_endian(5729, 'big'))

    def test_conv_endian_little_neg(self):
        """Tests conv_endian function for negative little endian."""
        self.assertEqual('-32 6B', task.conv_endian(-27442, 'little'))

    def test_conv_endian_big_neg(self):
        """Tests conv_endian function for negative big endian."""
        self.assertEqual('-16 61', task.conv_endian(-5729, 'big'))

    def test_conv_endian_random_pos(self):
        """Tests conv_endian function for random positive values."""
        endian = random.choice(['little', 'big'])
        num = random.randrange(0, 1000000)  # negative million to positive million, random number
        hex_str = str(hex(num)).upper()[2:]
        hex_list = []
        if len(hex_str) % 2:
            hex_str = '0' + hex_str
        byte = ''
        for index in range(len(hex_str)):
            byte = byte + hex_str[index]
            if index % 2:
                hex_list.append(byte)
                byte = ''
        if endian == 'little':
            hex_num = ' '.join(map(str, hex_list[::-1]))
        else:
            hex_num = ' '.join(map(str, hex_list))

        self.assertEqual(hex_num, task.conv_endian(num, endian))

    def test_conv_endian_random_neg(self):
        """Tests conv_endian function for random positive values."""
        endian = random.choice(['little', 'big'])
        num = random.randrange(-1000000, -1)          # negative million to positive million, random number
        hex_str = str(hex(num)).upper()[3:]
        hex_list = []
        if len(hex_str) % 2:
            hex_str = '0' + hex_str
        byte = ''
        for index in range(len(hex_str)):
            byte = byte + hex_str[index]
            if index % 2:
                hex_list.append(byte)
                byte = ''
        if endian == 'little':
            hex_num = ' '.join(map(str, hex_list[::-1]))
        else:
            hex_num = ' '.join(map(str, hex_list))
        hex_num = '-' + hex_num
        self.assertEqual(hex_num, task.conv_endian(num, endian))


if __name__ == '__main__':
    unittest.main()
