
def base_minus_2(num):
    if num == 0:
        return "0"

    result = ""
    while num != 0:
        if num % 2 == 0:
            result += "0"
        else:
            result += "1"
            num -= 1
        num //= -2

    return result[::-1]


if __name__ == "__main__":
    num = int(input())
    print(base_minus_2(num))
