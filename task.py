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
    days_remaining = num_sec // 86400
    leap_year_dict = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30,
                      '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
    comm_year_dict = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30,
                      '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
    year_to_return = '1970'
    month_to_return = '01'
    days_to_return = '01'
    year = int(year_to_return)
    while days_remaining > 0:
        # set year calendar
        current_dict = comm_year_dict
        if year % 100 == 0:
            if year % 400 == 0:
                current_dict = leap_year_dict
        elif year % 4 == 0:
            current_dict = leap_year_dict

        # iterate through days, and months till date reached, repeat from beginning at year-end
        for current_month in current_dict.keys():
            end_of_month_date = current_dict[current_month]
            if days_remaining > end_of_month_date:
                days_remaining = days_remaining - end_of_month_date
                continue
            else:
                month_to_return = current_month
                days_to_return = days_remaining + 1
                return str(month_to_return) + '-' + str(days_to_return) + '-' + str(year)
        year += 1
    return str(month_to_return) + '-' + str(days_to_return) + '-' + str(year)


def conv_endian(num, endian='big'):
    """
    This function takes in an integer value as 'num' and converts it to a
    hexadecimal number. Endian type is determined by the flag 'endian'.
    """
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    big_end_byte_arr = []
    current_byte = ''
    if num < 0:
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
