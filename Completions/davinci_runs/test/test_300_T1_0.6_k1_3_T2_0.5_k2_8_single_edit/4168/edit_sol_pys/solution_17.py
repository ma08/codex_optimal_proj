

def base_minus_2(n):
    if n == 0:
        return 0

    res = ""
    while n != 0:
        if n % 2 == 0:
            res += 0
        else:
            res += 1
            n -= 1
        n //= -2

    return int(res[::-1])


if __name__ == "__main__":
    n = int(input())
    print(base_minus_2(n))
