def char_to_int(char):
    """
    Helper function for conv_num. Takes a string character
    that is either hexadecimal or deciaml and returns its value as an int.
    """
    if '0' <= char <= '9':
        return ord(char) - 48
    elif 'a' <= char <= 'f':
        return ord(char) - 87
    else:
        return None


def conv_hexa(hexa_str):
    """
    Helper fucntion for conv_num. Takes a hexadecimal string and converts
    it to a decimal number.
    """
    hexa_num = 0
    hexa_length = len(hexa_str)
    exp = 0
    while exp < hexa_length:
        # iterate backwards through hex_str using exp
        char = hexa_str[hexa_length - 1 - exp]
        value = char_to_int(char)
        if value is None:
            return None

        hexa_num += value * (16 ** exp)
        # increase 16 exponent for next hexadecimal position
        exp += 1

    return hexa_num


def conv_num(num_str):
    """
    This function takes in a string and converts it into a base 10 number
    and returns it. Returns None if string is an invalid format.
    """

    # empty string check
    if not num_str:
        return None

    converted_num = 0

    # negative check
    negative_check = num_str.startswith("-")
    # remove negative from string
    if negative_check:
        num_str = num_str[1:]

    # hexadecimal check
    if num_str.lower().startswith("0x"):
        # omit first two characters of hexadecimal string
        hexa_str = num_str[2:].lower()
        converted_num = conv_hexa(hexa_str)

    else:
        # decimal conversion
        # multipliers to move to different base-10 digits
        tens_multiplier = 1
        tenths_multiplier = 0.1

        # decimal check
        decimal_count = num_str.count('.')

        if decimal_count == 1:
            # split string into whole number and fractional number str
            whole_num, fraction_num = num_str.split('.')
            # add decimal place for strings ending with '.'
            converted_num += 0.0
        else:
            whole_num = num_str
            fraction_num = ""

        # iterate through whole_num backwards to ascend through base-10 digits
        for char in reversed(whole_num):
            value = char_to_int(char)
            if value is None:
                return None

            converted_num += value * tens_multiplier

            # move to next base-10 position
            tens_multiplier *= 10

        # iterate through fraction_num to descend through base-10 digits
        for char in fraction_num:
            value = char_to_int(char)
            if value is None:
                return None
            converted_num += value * tenths_multiplier
            # move to next base-10 position
            tenths_multiplier *= 0.1

    return -converted_num if negative_check else converted_num


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
    This function takes in an integer value as 'num' and converts it to a
    hexadecimal number. Endian type is determined by the flag 'endian'.
    """
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    big_end_byte_arr = []
    current_byte = ''
    if num < 0:             # negative check
        neg_flag = True
        dec_num = -num
    else:
        neg_flag = False
        dec_num = num
    while True:                                                         # loop till decimal is 0
        current_byte = hex_dict[dec_num % 16] + current_byte
        dec_num = dec_num//16
        if len(current_byte) == 2:                                      # byte val found, wrap and reset byte container
            big_end_byte_arr.insert(0, current_byte)
            current_byte = ''
        if dec_num < 16:                                                # end of num reached, save and break
            current_byte = hex_dict[dec_num % 16] + current_byte
            if len(current_byte) == 1:                                  # leading zero for byte
                current_byte = '0' + current_byte
            big_end_byte_arr.insert(0, current_byte)
            break

    if endian == 'big':
        hex_num = ' '.join(map(str, big_end_byte_arr))
    elif endian == 'little':
        hex_num = ' '.join(map(str, big_end_byte_arr[::-1]))               # flip order on little endian
    else:
        raise Exception("Endian type can only be 'little' or 'big'.")

    if neg_flag:
        hex_num = '-' + hex_num
    return hex_num
