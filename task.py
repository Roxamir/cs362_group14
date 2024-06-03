def conv_num(num_str):
    """
    This function takes in a string and converts it into a base 10 number
    and returns it. Returns None if string is an invalid format.
    """
    pass


def my_datetime(num_sec):
    """
    This function takes an integer value that represents the number of seconds
    since the epoch: January 1st, 1970. Takes 'num_sec', converts to date and
    returns it as a string with the format MM-DD-YYYY.
    """
    # Special case: if num_sec is 0, return '01-01-1970'
    if num_sec == 0:
        return "01-01-1970"
    # Convert seconds to days
    days_remaining = num_sec // 86400
    current_year = 1970

    # Dictionaries for days in months for leap and regular years
    leap_year_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    reg_year_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # Helper function to check for leap year

    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    while days_remaining > 0:
        if is_leap_year(current_year):
            curr_dict = leap_year_dict
        else:
            curr_dict = reg_year_dict
        for month in range(1, 13):  # 1 to 12 for months
            days_in_month = curr_dict[month]
            if days_remaining >= days_in_month:
                days_remaining -= days_in_month
            else:
                month_to_return = month
                day_to_return = days_remaining + 1  # days are 1-indexed
                return f"{month_to_return:02d}-{day_to_return:02d}-{current_year}"
        current_year += 1
        # If we exit the while loop, it means we need to return the result for the remaining days
    return f"{1:02d}-{days_remaining + 1:02d}-{current_year}"


def conv_endian(num, endian='big'):
    """
    This function takes in an integer value as 'num' and conferts it to a
    hexadecimal number. Endian type is determined by the flag 'endian'.
    """
    pass

