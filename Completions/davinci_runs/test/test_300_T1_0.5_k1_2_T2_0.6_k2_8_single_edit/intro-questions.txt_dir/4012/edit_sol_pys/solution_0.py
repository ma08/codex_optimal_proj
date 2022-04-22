

def main():
    print(calculate(1, 2, 4))


def calculate(a, b, c):
    res = 0
    while b % a != 0 and c % b != 0:
        if b % a != 0:
            b += 1
            res += 1
        if c % b != 0:
            c += 1
            res += 1
    return res, b, c


if __name__ == '__main__':
    main()
