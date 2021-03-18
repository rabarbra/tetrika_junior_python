#-*- encoding: utf-8 -*-

def task(array):
    size = len(array)
    if size == 1 and array[0] == '0':
        return(0)
    elif size <= 1 or array[size - 1] == '1':
        raise ValueError('Zero not found!')
    flag = (size - 1) // 2
    buf = size - 1
    while array[flag] == array[flag + 1] and flag != 0:
        if array[flag] == '0':
            buf = flag
            flag = flag // 2
        else:
            flag = flag + (buf - flag) // 2
    result = 0 if flag == 0 and array[flag] == '0' else flag + 1
    return(result)
