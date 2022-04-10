

import sys
import math

# def main(a):
#     n = 1
#     while True:
#         if a <= 2**n:
#             return n
#         n += 1

def main(a):
    return math.floor(math.log(a, 2)) + 1


if __name__ == "__main__":
    a = int(sys.stdin.readline().strip())
    print(main(a))