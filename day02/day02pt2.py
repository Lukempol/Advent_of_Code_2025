def is_valid_v2(num):
    num_str = str(num)
    size = int(len(num_str))
    for div in range(1,size//2):
        if size % div != 0:
            continue
        previous_num = num_str[:div]
        for i in range(0, size, div):
            current_num = num_str[i:i+div]
            digits_repeat = current_num == previous_num
            if not digits_repeat:
                break
        if digits_repeat:
            return True
    return False
