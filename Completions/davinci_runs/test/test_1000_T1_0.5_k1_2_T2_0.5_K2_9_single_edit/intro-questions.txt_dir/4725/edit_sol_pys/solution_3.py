#!/usr/bin/env python3


# import sys
#
# def main():
#     input = sys.stdin.readline().strip()
#     if len(input) <= 2:
#         print(0)
#     else:
#         chars = set()
#         for i in range(len(input)):
#             if input[i] not in chars:
#                 chars.add(input[i])
#             if len(chars) > 2:
#                 print(i)
#                 return
#         print(len(input))
#
# if __name__ == '__main__':
#     main()

#!/usr/bin/env python3

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main(n):
    for i in range(n):
        if is_prime(i):
            print(i)


if __name__ == "__main__":
    n = int(input())
    main(n)
