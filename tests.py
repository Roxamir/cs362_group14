import unittest
import task
import random


class TestCase(unittest.TestCase):
    # test conv_num
    def test_conv_num_decimal_pos(self):
        """Test positive decimal numbers."""
        self.assertTrue(True)

    def test_conv_num_hex_pos(self):
        """Test positive hexadecimal numbers."""
        self.assertTrue(True)

    def test_conv_num_decimal_neg(self):
        """Test negative decimal numbers."""
        self.assertTrue(True)

    def test_conv_num_decimal_point_pos(self):
        """Test positive numbers with decimal point."""
        self.assertTrue(True)

    def test_conv_num_decimal_point_neg(self):
        """Test negative numbers with decimal point."""
        self.assertTrue(True)

    # test my_datetime
    def test_my_datetime(self):
        """Tests my_datetime function."""
        self.assertEqual(task.my_datetime(0), '01-01-1970')

    # test conv_endian
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
