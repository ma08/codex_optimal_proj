


def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a


def check_increase(a):
    if len(a) == 0:
        return True
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            return False
    return True


def check_decrease(a):
    if len(a) == 0:
        return True
    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:
            return False
    return True


def check_input(n, a):
    if n == 0:
        return True
    for i in range(1, n):
        if a[i] != a[i - 1]:
            return True
    return False


def split(n, a):
    inc = []
    dec = []
    inc_len = 0
    dec_len = 0
    for i in range(n):
        if i % 2 == 0:
            inc.append(a[i])
            inc_len += 1
        else:
            dec.append(a[i])
            dec_len += 1
    return inc_len, inc, dec_len, dec


def main():
    n, a = get_input()
    if check_input(n, a):
        inc_len, inc, dec_len, dec = split(n, a)
        if check_increase(inc) and check_decrease(dec):
            print("YES")
            print(inc_len)
            print(*inc)
            print(dec_len)
            print(*dec)
        else:
            print("NO")
    else:
        print("NO")


if __name__ == '__main__':
    main()