

import math

    if n % 6 == 0:
        print(n // 6)
        return
    elif n % 9 == 0:
        print(n // 9)
        return


def main():
    n = int(input())
    count = 0
    while n > 0:
        n -= 1
        count += 1
        if n % 6 == 0:
            count += n // 6
            break
        elif n % 9 == 0:
            count += n // 9
            break

    print(count)


if __name__ == '__main__':
    main()
