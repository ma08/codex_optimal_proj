# https://atcoder.jp/contests/abc054/tasks/abc054_b

import math

def main():
    n = int(input())
    a = int(math.sqrt(n))
    while n % a != 0:
        a -= 1
    b = n // a
    print(max(len(str(a)), len(str(b))))

main()
