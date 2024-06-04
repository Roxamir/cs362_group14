def conv_num(num_str):
    """
    This function takes in a string and converts it into a base 10 number
    and returns it. Returns None if string is an invalid format.
    """

    def char_to_int(char):
        if '0' <= char <= '9':
            return ord(char) - 48
        elif 'a' <= char <= 'f':
            return ord(char) - 87
        else:
            return None

    def conv_hexa(hexa_str):
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

    # empty string check
    if not num_str:
        return None

    # negative check
    negative_check = num_str.startswith("-")
    # remove negative from string
    if negative_check:
        num_str = num_str[1:]

    # hexadecimal check
    if num_str.lower().startswith("0x"):
        # omit first two characters of hexadecimal string
        hexa_str = num_str[2:].lower()
        hexa_num = conv_hexa(hexa_str)

        return -hexa_num if negative_check else hexa_num

    # decimal conversion
    # multipliers to move to different base-10 digits
    tens_multiplier = 1
    tenths_multiplier = 0.1

    decimal_num = 0
    # decimal check
    decimal_count = num_str.count('.')

    if decimal_count == 1:
        # split string into whole number and fractional number str
        whole_num, fraction_num = num_str.split('.')
        # add decimal place for strings ending with '.'
        decimal_num += 0.0
    else:
        whole_num = num_str
        fraction_num = ""

    # iterate through whole_num backwards to ascend through base-10 digits
    for char in reversed(whole_num):
        value = char_to_int(char)
        if value is None:
            return None

        decimal_num += value * tens_multiplier

        # move to next base-10 position
        tens_multiplier *= 10

    # iterate through fraction_num to descend through base-10 digits
    for char in fraction_num:
        value = char_to_int(char)
        if value is None:
            return None
        decimal_num += value * tenths_multiplier
        # move to next base-10 position
        tenths_multiplier *= 0.1

    return -decimal_num if negative_check else decimal_num


def my_datetime(num_sec):
    """
    This function takes an integer value that represents the number of seconds
    since the epoch: January 1st, 1970. Takes 'num_sec', converts to date and
    returns it as a string with the format MM-DD-YYYY.
    """
    pass


def conv_endian(num, endian='big'):
    """
    This function takes in an integer value as 'num' and conferts it to a
    hexadecimal number. Endian type is determined by the flag 'endian'.
    """
    pass
