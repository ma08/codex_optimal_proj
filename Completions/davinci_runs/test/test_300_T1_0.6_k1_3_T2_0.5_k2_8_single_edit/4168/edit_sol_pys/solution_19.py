
def base_minus_2(num):
    if num == 0:
        return "0"

    res = ""
    while num != 0:
        if num % 2 == 0:
            res += "0"
        else:
            res += "1"
            num -= 1
        num //= -2

    return res[::-1]


if __name__ == "__main__":
    num = int(input())
    print(base_minus_2(num))
