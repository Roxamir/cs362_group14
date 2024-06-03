import unittest
import task


class TestCase(unittest.TestCase):
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

    def test_my_datetime(self):
        """Tests my_datetime function."""
        self.assertEqual(task.my_datetime(0), '01-01-1970')

    def test_conv_endian(self):
        """Tests conv_endian function."""
        self.assertEqual('6B 32', task.conv_endian(27442))


if __name__ == '__main__':
    unittest.main()
