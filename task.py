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
