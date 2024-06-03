def conv_num(num_str):
    """
    This function takes in a string and converts it into a base 10 number
    and returns it. Returns None if string is an invalid format.
    """

    decimal_num = 0

    # empty string check
    if not num_str:
        return None

    # negative check
    if num_str[0] == '-':
        negative_check = True
        # remove negative from string
        num_str = num_str[1:]
    else:
        negative_check = False

    num_length = len(num_str)
    decimal_count = 0

    for i in range(num_length):
        # decimal check
        if num_str[i] == ".":
            decimal_count += 1

        if decimal_count > 1:
            return None

    # hexadecimal check
    if num_str.lower().startswith("0x"):
        # check if hexadecimal section is empty
        if num_length == 2:
            return None
        hex_num = 0
        # omit first two characters of hexadecimal string
        hexa_str = num_str[2:].lower()
        exp = 0

        # hexadecimal conversion
        # iterating through string backwards to handle 16^exp
        for char in reversed(hexa_str):
            if '0' <= char <= '9':
                # ord(0) = 48. subtract 48 to get int value
                hex_num += (ord(char) - 48) * (16 ** exp)

            elif 'a' <= char <= 'f':
                # ord('a') = 97, subtract 87 to get hexadecimal values
                hex_num += (ord(char) - 87) * (16 ** exp)

            else:
                return None
            # increase 16 exponent for next hexadecimal position
            exp += 1
        return -hex_num if negative_check else hex_num

    # decimal conversion
    # multipliers to move to different base-10 digits
    tens_multiplier = 1
    tenths_multiplier = 0.1

    if decimal_count >= 0:
        if decimal_count == 1:
            # split string into whole number and fractional number str
            whole_num, fraction_num = num_str.split('.')
        else:
            whole_num = num_str
        # iterate through whole_num backwards to ascend through base-10 digits
        for char in reversed(whole_num):
            if char < '0' or char > '9':
                return None

            else:
                decimal_num += (ord(char) - 48) * tens_multiplier

            # move to next base-10 position
            tens_multiplier *= 10
        if decimal_count != 0:
            # iterate through fraction_num to descend through base-10 digits
            for char in fraction_num:
                if '0' <= char <= '9':
                    decimal_num += (ord(char) - 48) * tenths_multiplier

                else:
                    return None

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


if __name__ == "__main__":

    print(conv_num('12345'))       # returns 12345
    print(conv_num('-123.45'))     # returns -123.45
    print(conv_num('.45'))         # returns 0.45
    print(conv_num('123.'))        # returns 123.0
    print(conv_num('0xAD4'))       # returns 2772
    print(conv_num('0Xad4'))       # returns 2772
    print(conv_num('0xAZ4'))       # returns None
    print(conv_num('12345A'))      # returns None
    print(conv_num('12.3.45'))     # returns None
