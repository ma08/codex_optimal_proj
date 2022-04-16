
def get_input():

    n = int(input())
    a = list(map(int, input().split()))
    return n, a


def check_increase(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))


def check_decrease(a):
    return all(a[i] >= a[i + 1] for i in range(len(a) - 1))


def check_input(n, a):
    return any(a[i] != a[i + 1] for i in range(n - 1))


def split(n, a):
    inc = []
    dec = []
    for i in range(n):
        if i % 2 == 0:
            inc.append(a[i])
        else:
            dec.append(a[i])
    return len(inc), inc, len(dec), dec


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
