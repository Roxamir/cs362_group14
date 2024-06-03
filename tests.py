import unittest
from task import my_datetime  # Replace 'your_module' with the actual module name where my_datetime is defined


class TestMyDatetime(unittest.TestCase):

    def test_epoch_start(self):
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_non_leap_year(self):
        # January 2, 1970
        self.assertEqual(my_datetime(86400), '01-02-1970')
        # December 31, 1970
        self.assertEqual(my_datetime(31536000 - 86400), '12-31-1970')

    def test_leap_year(self):
        # January 1, 1972
        self.assertEqual(my_datetime(63072000), '01-01-1972')
        # March 1, 1972 (68256000 seconds calculated previously)
        self.assertEqual(my_datetime(68256000), '03-01-1972')

    def test_boundary_conditions(self):
        # December 31, 1971
        self.assertEqual(my_datetime(63072000 - 86400), '12-31-1971')
        # January 1, 1973
        self.assertEqual(my_datetime(94608000), '12-31-1972')

    def test_large_number_of_seconds(self):
        # January 1, 2000
        self.assertEqual(my_datetime(946684800), '01-01-2000')
        # January 1, 2020
        self.assertEqual(my_datetime(1577836800), '01-01-2020')

    def test_known_dates(self):
        # July 20, 1969, in seconds since epoch would be negative (before 1970), so we'll skip this test
        # Some other known dates
        self.assertEqual(my_datetime(1234567890), '02-13-2009')
        self.assertEqual(my_datetime(1500000000), '07-14-2017')


if __name__ == '__main__':
    unittest.main()
