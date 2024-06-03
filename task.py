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

