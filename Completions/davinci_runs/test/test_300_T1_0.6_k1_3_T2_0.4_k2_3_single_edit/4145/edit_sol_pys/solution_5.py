def prime(num):
    if num == 2:
        return 2
    if num % 2 == 0:
        num += 1
    while True:
        if num == 3:
            return 3
        if num == 5:
            return 5
        if num == 7:
            return 7
        if num == 11:
            return 11
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
            num = num + 2
            continue
        else:
            return num
            break
