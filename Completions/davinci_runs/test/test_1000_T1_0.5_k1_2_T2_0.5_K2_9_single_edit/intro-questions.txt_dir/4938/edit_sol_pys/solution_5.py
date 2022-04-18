def max_ex_length(s, x):
    w = 0
    m = 0
    i = 0


    for c in s:
        if c == 'W':
            w += 1
        else:
            m += 1
        if abs(w - m) > x:
            break
        i += 1

    return i


print(i)
