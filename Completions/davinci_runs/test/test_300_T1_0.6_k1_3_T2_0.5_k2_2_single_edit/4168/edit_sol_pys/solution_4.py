

def convert_base(num, base):
    if num < 0:
        num = -num
        sign = -1
    else:
        sign = 1

    res = ""
    while num > 0:
        rem = num % base
        num //= base
        if rem < 10:
            res += chr(ord('0') + rem)
        else:
            res += chr(ord('A') + rem - 10)

    if sign == -1:
        res += '-'

    return res[::-1] if res else "0"


if __name__ == "__main__":
    print(convert_base(int(input()), -2))
