def conv_num(num_str):
    """
    This function takes in a string and converts it into a base 10 number
    and returns it. Returns None if string is an invalid format.
    """
    return True


def my_datetime(num_sec):
    """
    This function takes an integer value that represents the number of seconds
    since the epoch: January 1st, 1970. Takes 'num_sec', converts to date and
    returns it as a string with the format MM-DD-YYYY.
    """
    return '01-01-1970'


def conv_endian(num, endian='big'):
    """
    This function takes in an integer value as 'num' and converts it to a
    hexadecimal number. Endian type is determined by the flag 'endian'.
    """
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_byte_list = []
    current_byte = ''
    dec_num = num
    while True:                                                         # loop till decimal is 0
        current_byte = hex_dict[dec_num % 16] + current_byte
        dec_num = dec_num//16
        if len(current_byte) == 2:                                      # byte val found, wrap and reset byte container
            hex_byte_list.insert(0, current_byte)
            current_byte = ''
        if dec_num < 16:                                                # end of num reached, save and break
            current_byte = hex_dict[dec_num % 16] + current_byte
            if len(current_byte) == 1:
                current_byte = '0' + current_byte
            hex_byte_list.insert(0, current_byte)
            break

    if endian == 'big':
        hex_num = ' '.join(map(str, hex_byte_list))
    elif endian == 'little':
        hex_num = ' '.join(map(str, hex_byte_list[::-1]))
    else:
        raise Exception("Endian type can only be 'little' or 'big'.")

    return hex_num
